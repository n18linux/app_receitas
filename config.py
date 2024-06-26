DEBUG=True
USERNAME='root'
PASSWORD=''
SERVER='localhost'
DB='db_app_receitas'

SQLALCHEMY_DATABASE_URI=f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'

# Permite que as migrações aconteçam em tempo real entre as tabelas mysql.
SQLALCHEMY_TRACK_MODIFICATIONS=True


# Chave para funçõesd importantes da aplicação
SECRET_KEY='chave_secreta1'