import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SMTP_SERVER = os.environ.get('SMTP_SERVER') or 'smtp.example.com'
    SMTP_PORT = os.environ.get('SMTP_PORT') or 587
    SMTP_USERNAME = os.environ.get('SMTP_USERNAME') or 'your_email@example.com'
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD') or 'your_password'
    FIREBASE_CREDENTIALS = os.environ.get('FIREBASE_CREDENTIALS') or 'path/to/firebase/credentials.json'