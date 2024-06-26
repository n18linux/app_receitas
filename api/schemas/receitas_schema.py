from api import ma
from marshmallow import fields
from api.models import receitas_model
from api.schemas import alimentos_schema
from api.schemas import refeicao_schema

class ReceitaSchema(ma.SQLAlchemyAutoSchema):

    alimento = ma.Nested('AlimentoSchema', only=("nome", "caloria", "proteina"))

    class Meta:
        model =  receitas_model.Receita
        load_instance = True
        include_fk = True

    nome = fields.String(required=False)
    caloria = fields.Float(required=False)
    proteina = fields.Float(required=False)
    alimentos_id = fields.Integer(required=True)