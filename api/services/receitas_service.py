# Arquivo: services/receitas_service.py
from ..models import receitas_model
from api import db

def listar_receitas():
    return receitas_model.Receitas.query.all()

def listar_receitas_id(id):
    return receitas_model.Receitas.query.filter_by(id=id).first()

def cadastrar_receita(receita):
    nova_receita = receitas_model.Receitas(nome=receita.nome,
                                           caloria=receita.caloria,
                                           proteina=receita.proteina,
                                           carboidrato=receita.carboidrato,
                                           gordura=receita.gordura,
                                           fibra=receita.fibra,
                                           grupo=receita.grupo,
                                           grama=receita.grama,
                                           colherSopa=receita.colherSopa,
                                           unidadePedacoMedida=receita.unidadePedacoMedida,
                                           tempoPreparo=receita.tempoPreparo,
                                           modo_preparo=receita.modo_preparo,
                                           imagem=receita.imagem,
                                           alimentos=receita.alimentos)
    db.session.add(nova_receita)
    db.session.commit()
    return nova_receita

def atualizar_receita(receita_bd, receita_nova):
    receita_bd.nome = receita_nova.nome
    receita_bd.caloria = receita_nova.caloria
    receita_bd.proteina = receita_nova.proteina
    receita_bd.carboidrato = receita_nova.carboidrato
    receita_bd.gordura = receita_nova.gordura
    receita_bd.fibra = receita_nova.fibra
    receita_bd.grupo = receita_nova.grupo
    receita_bd.grama = receita_nova.grama
    receita_bd.colherSopa = receita_nova.colherSopa
    receita_bd.unidadePedacoMedida = receita_nova.unidadePedacoMedida
    receita_bd.tempoPreparo = receita_nova.tempoPreparo
    receita_bd.modo_preparo = receita_nova.modo_preparo
    receita_bd.imagem = receita_nova.imagem
    receita_bd.alimentos = receita_nova.alimentos

    db.session.commit()
    return receita_bd

def excluir_receita(receita):
    db.session.delete(receita)
    db.session.commit()
