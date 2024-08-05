from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import bcrypt
from Config import Config
import requests
import logging
from dotenv import load_dotenv
import os
## from generate_keys import generate_password_hash, generate_secret_key
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return redirect(url_for('success'))
        else:
            error = "Usuario o Contraseña incorrectos, intentelo de nuevo."
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    success = None
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            error = "Nombre de usuario existente. Intentalo con otro diferente"
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            success = "Te has registrado correctamente."
    return render_template('register.html', success=success, error=error)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password')  # Usa .get() para evitar KeyError
        if password and bcrypt.checkpw(password.encode('utf-8'), Config.ADMIN_PASSWORD_HASH.encode('utf-8')):
            return redirect(url_for('view_users'))
        else:
            error = "Contraseña incorrecta de admin, intentalo de nuevo."
    return render_template('admin_login.html', error=error)

@app.route('/admin/users')
def view_users():
    users = User.query.all()
    return render_template('view_users.html', users=users)

@app.route('/show_weather')
def show_weather():
    api_key = os.getenv('WEATHER_API_KEY')
    city = "Buenos Aires"  # puedes elegir la que quieras
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
    with app.app_context():
        create_tables()
    app.run(debug=True)
