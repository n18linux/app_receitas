from api import ma
from marshmallow import fields
from api.models import refeicao_model


class RefeicaoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model =  refeicao_model.Refeicao
        load_instance = True

        nome = fields.String(required=True)
        horario = fields.Time(required=True)
        idDietaPronta = fields.Integer(required=False)
        idReceita = fields.Integer(required=False)
        idAlimento = fields.Integer(required=False)
