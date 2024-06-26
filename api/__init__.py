from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config.from_object('config')

# Biblioteca JWT Manager cuida do Login
jwt = JWTManager(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
mi = Migrate(app,db)
api = Api(app)


from .models import alimentos_model
from .views import alimentos_view


from .models import receitas_model
from .views import receitas_view


from .models import refeicao_model
from .views import refeicao_view