DEBUG=True

USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
DB = 'db_app_receitas'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'chave_secreta1'