import bcrypt

password = 'admin' 

# Genera el hash de la contraseña
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Imprime el hash en la consola
print(hashed.decode('utf-8'))
