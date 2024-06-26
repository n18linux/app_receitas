from api import db


class Alimento(db.Model):
    __tablename__ = 'tb_alimento'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(90), nullable=False)
    caloria = db.Column(db.Float, nullable=False)
    proteina = db.Column(db.Float, nullable=False)

    receitas = db.relationship("Receita", back_populates="alimento")