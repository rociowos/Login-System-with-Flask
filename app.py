from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import bcrypt
from Config import Config
import requests
import logging
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
app.config.from_object(Config)

# Conectar con la base de datos MySQL
import MySQLdb
db = MySQLdb.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
            return redirect(url_for('success'))
        else:
            error = "Usuario o Contraseña incorrectos, intentelo de nuevo."
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    success = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            cursor.close()
            error = "Nombre de usuario existente. Inténtalo con otro diferente."
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') #encriptar pass
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            db.commit()
            cursor.close()
            success = "Te has registrado correctamente."
    return render_template('register.html', error=error, success=success)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password')  
        if password and bcrypt.checkpw(password.encode('utf-8'), Config.ADMIN_PASSWORD_HASH.encode('utf-8')):
            return redirect(url_for('view_users'))
        else:
            error = "Contraseña incorrecta de admin, intentalo de nuevo."
    return render_template('admin_login.html', error=error)


@app.route('/admin/users')
def view_users():
    cursor = db.cursor()
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()
    cursor.close()
    return render_template('view_users.html', users=users)



@app.route('/show_weather')
def show_weather():
    api_key = os.getenv('WEATHER_API_KEY')
    city = "Buenos Aires" #podes elegir la que quieras
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        if response.status_code == 200:
            weather = {
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'city': data['name']
            }
            return render_template('show_weather.html', weather=weather)
        elif response.status_code == 401:
            return "Clave de API no válida", 401
        else:
            return "Error desconocido en la API del clima", response.status_code
    except requests.RequestException as e:
        return f"Error al obtener datos del clima: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)



#correr el programa con: python app.py
