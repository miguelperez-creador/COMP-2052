import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_segura'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'mysql+pymysql://root:root@localhost/gestor_biblioteca'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
