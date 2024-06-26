from api import ma
from api.models  import alimentos_model
from marshmallow import fields
from api.schemas import receitas_schema

class AlimentoSchema(ma.SQLAlchemyAutoSchema):
    #receitas = ma.Nested(receitas_schema.ReceitaSchema, many=True, only=("nome", "caloria", "proteina"))
    #receitas = ma.Nested('ReceitaSchema', only=("nome", "caloria"))
    class Meta:
        model = alimentos_model.Alimento
        load_instance = True

    nome = fields.String(required=True)
    caloria = fields.Float(required=True)
    proteina = fields.Float(required=True)