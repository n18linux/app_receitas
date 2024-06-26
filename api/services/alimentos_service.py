from api import db
from ..models import alimentos_model


def listar_alimentos():
    _alimentos = alimentos_model.Alimento.query.all()
    return _alimentos

def listar_alimento_id(id):
    _alimentos = alimentos_model.Alimento.query.filter_by(id=id).first()
    return _alimentos

def cadastrar_alimento(alimento):
    alimento_bd = alimentos_model.Alimento(
        nome=alimento.nome,
        caloria=alimento.caloria,
        proteina=alimento.proteina
    )
    db.session.add(alimento_bd)
    db.session.commit()
    return alimento_bd

def atualizar_alimento(alimento, alimento_novo):
    alimento.nome = alimento_novo.nome
    alimento.caloria = alimento_novo.caloria
    alimento.proteina = alimento_novo.proteina

    db.session.commit()
    return alimento

def exclui_alimento(alimento):
    db.session.delete(alimento)
    db.session.commit()




