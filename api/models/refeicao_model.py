from api import db


class Refeicao(db.Model):
    __tablename__ = 'tb_refeicao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(90), nullable=False)
    horario = db.Column(db.Time, nullable=False)
    idDietaPronta = db.Column(db.Integer, nullable=True)
    idReceita = db.Column(db.Integer, nullable=True)
    alimentos_id = db.Column(db.Integer, nullable=True)  # Aqui deveria ser a lista de Alimentos