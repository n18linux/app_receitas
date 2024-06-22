# Arquivo: models/receitas_model.py
from api import db

class Receitas(db.Model):
    __tablename__ = "receitas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    caloria = db.Column(db.Float, nullable=False)
    proteina = db.Column(db.Float, nullable=False)
    carboidrato = db.Column(db.Float, nullable=False)
    gordura = db.Column(db.Float, nullable=False)
    fibra = db.Column(db.Float, nullable=False)
    grupo = db.Column(db.String(45), nullable=False)
    grama = db.Column(db.Float, nullable=False)
    colherSopa = db.Column(db.Float, nullable=False)
    unidadePedacoMedida = db.Column(db.Float, nullable=False)
    tempoPreparo = db.Column(db.String(5), nullable=False)
    modo_preparo = db.Column(db.String(255), nullable=False)
    imagem = db.Column(db.String(255), nullable=False)
    # Relacionamento com a tabela de alimentos
    alimentos = db.relationship('Alimentos', secondary='receita_alimentos', lazy='subquery',
                                   backref=db.backref('receitas', lazy=True))
