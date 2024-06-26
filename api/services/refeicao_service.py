from api import db
from ..models import refeicao_model


def listar_refeicoes():
    _refeicoes = refeicao_model.Refeicao.query.all()
    return _refeicoes

def listar_refeicoes_id(id):
    _refeicoes = refeicao_model.Refeicao.query.filter_by(id=id).first()
    return _refeicoes

def cadastrar_refeicao(refeicao):
    refeicao_bd = refeicao_model.Refeicao(
        nome=refeicao.nome,
        horario=refeicao.horario,
        idDietaPronta=refeicao.idDietaPronta,
        idReceita=refeicao.idReceita,
        idAlimento = refeicao.idAlimento
    )
    db.session.add(refeicao_bd)
    db.session.commit()
    return refeicao_bd

def atualizar_refeicao(refeicao, refeicao_nova):
    refeicao.nome = refeicao_nova.nome
    refeicao.horario = refeicao_nova.horario
    refeicao.idDietaPronta = refeicao_nova.idDietaPronta
    refeicao.idReceita = refeicao_nova.idReceita
    refeicao.idAlimento = refeicao_nova.idAlimento

    db.session.commit()
    return refeicao

def exclui_refeicao(refeicao):
    db.session.delete(refeicao)
    db.session.commit()




