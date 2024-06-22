from ..models import alimentos_model
from api import db

def listar_alimentos():
    alimentos = alimentos_model.Alimentos.query.all()
    return alimentos

def listar_alimentos_id(id):
    alimentos = alimentos_model.Alimentos.query.filter_by(id=id).first()
    return alimentos



def cadastrar_alimento(alimento):
    alimento_bd = alimentos_model.Alimentos(nome=alimento.nome,
                                            caloria=alimento.caloria,
                                            proteina=alimento.proteina,
                                            carboidrato=alimento.carboidrato,
                                            gordura=alimento.gordura,
                                            fibra=alimento.fibra,
                                            grupo=alimento.grupo,
                                            grama=alimento.grama,
                                            colherSopaCheia=alimento.colherSopaCheia,
                                            unidadeFatiaMedida=alimento.unidadeFatiaMedida,
                                            mililitros=alimento.mililitros)
    db.session.add(alimento_bd)
    db.session.commit()
    return alimento_bd


def atualizar_alimento(alimento, alimento_novo):
    alimento.nome = alimento_novo.nome
    alimento.caloria = alimento_novo.caloria
    alimento.proteina = alimento_novo.proteina
    alimento.carboidrato = alimento_novo.carboidrato
    alimento.gordura = alimento_novo.gordura
    alimento.fibra = alimento_novo.fibra
    alimento.grupo = alimento_novo.grupo
    alimento.grama = alimento_novo.grama
    alimento.colherSopaCheia = alimento_novo.colherSopaCheia
    alimento.unidadeFatiaMedida = alimento_novo.unidadeFatiaMedida
    alimento.mililitros = alimento_novo.mililitros

    db.session.commit()
    return alimento

def exclui_alimento(alimento):
    db.session.delete(alimento)
    db.session.commit()