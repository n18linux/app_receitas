from api import db


class Receita(db.Model):
    __tablename__ = 'tb_receita'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(90), nullable=False)
    caloria = db.Column(db.Float, nullable=False)
    proteina = db.Column(db.Float, nullable=False)
    alimentos_id = db.Column(db.Integer, db.ForeignKey("tb_alimento.id")) # Aqui deveria ser a lista de Alimentos

    alimento = db.relationship("Alimento", back_populates="receitas")

