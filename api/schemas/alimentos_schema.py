from api import ma
from ..models import alimentos_model
from marshmallow import fields

class AlimentosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = alimentos_model.Alimentos
        load_instance = True

    nome = fields.String(required=True)
    caloria = fields.Float(required=False)
    proteina = fields.Float(required=False)
    carboidrato = fields.Float(required=False)
    gordura = fields.Float(required=False)
    fibra = fields.Float(required=False)
    grupo = fields.String(required=False)
    grama = fields.Float(required=False)
    colherSopaCheia = fields.Float(required=False)
    unidadePedacoMedida = fields.Float(required=False)
    milimetros = fields.Float(required=False)