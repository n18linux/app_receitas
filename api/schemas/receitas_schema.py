# Arquivo: schemas/receitas_schema.py
from api import ma
from ..models import receitas_model
from ..schemas.alimentos_schema import AlimentosSchema
from marshmallow import fields

class ReceitasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = receitas_model.Receitas
        load_instance = True

    nome = fields.String(required=True)
    caloria = fields.Float(required=True)
    proteina = fields.Float(required=True)
    carboidrato = fields.Float(required=True)
    gordura = fields.Float(required=True)
    fibra = fields.Float(required=True)
    grupo = fields.String(required=True)
    grama = fields.Float(required=True)
    colherSopa = fields.Float(required=True)
    unidadePedacoMedida = fields.Float(required=True)
    tempoPreparo = fields.String(required=True)
    modo_preparo = fields.String(required=True)
    imagem = fields.String(required=True)
    ingredientes = fields.Nested(AlimentosSchema, many=True, only=('id', 'nome', 'caloria', 'proteina', 'carboidrato',
                                                                  'gordura', 'fibra', 'grupo', 'grama', 'colherSopa',
                                                                  'unidadePedacoMedida', 'mililitros'))


