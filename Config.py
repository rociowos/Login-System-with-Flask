# config.py
from generate_keys import generate_password_hash, generate_secret_key

class Config:
    SECRET_KEY = generate_secret_key()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_PASSWORD_HASH = generate_password_hash('admin')
