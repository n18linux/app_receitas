from api import db
from ..models import receitas_model


def listar_receitas():
    _receitas = receitas_model.Receita.query.all()
    return _receitas

def listar_receita_id(id):
    _receitas = receitas_model.Receita.query.filter_by(id=id).first()
    return _receitas

def cadastrar_receita(receita):
    receita_bd = receitas_model.Receita(
        nome=receita.nome,
        caloria=receita.caloria,
        proteina=receita.proteina,
        alimentos_id=receita.alimentos_id
    )
    db.session.add(receita_bd)
    db.session.commit()
    return receita_bd

def atualizar_receita(receita, receita_nova):
    receita.nome = receita_nova.nome
    receita.caloria = receita_nova.caloria
    receita.proteina = receita_nova.proteina
    receita.alimentos_id = receita_nova.alimentos_id

    db.session.commit()
    return receita

def exclui_receita(receita):
    db.session.delete(receita)
    db.session.commit()




