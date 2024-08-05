# generate_keys.py
import bcrypt
import os
import binascii

def generate_password_hash(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')

def generate_secret_key() -> str:
    return binascii.hexlify(os.urandom(24)).decode()

# Generate keys
ADMIN_PASSWORD_HASH = generate_password_hash('admin')
SECRET_KEY = generate_secret_key()
