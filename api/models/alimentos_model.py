from api import db  # instância de SQLAlchemy chamada 'db'

class Alimentos(db.Model):
    __tablename__ = 'alimentos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    caloria = db.Column(db.Float, nullable=False)
    proteina = db.Column(db.Float, nullable=False)
    carboidrato = db.Column(db.Float, nullable=False)
    gordura = db.Column(db.Float, nullable=False)
    fibra = db.Column(db.Float, nullable=False)
    grupo = db.Column(db.String(50), nullable=False)
    grama = db.Column(db.Float)
    colher_sopa_cheia = db.Column(db.Float)
    unidade_fatia_medida = db.Column(db.Float)
    mililitros = db.Column(db.Float)
