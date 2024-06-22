from flask_restful import Resource
from ..schemas import alimentos_schema
from flask import request, make_response, jsonify
from ..entidades import alimentos
from ..services import alimentos_service
from api import api


class AlimentosList(Resource):

    # Mostra toda as informações dentro da tebela
    def get(self):
        alimento = alimentos_service.listar_alimentos()
        cs = alimentos_schema.AlimentosSchema(many=True)
        return make_response(cs.jsonify(alimento), 201)

    # Cria um novo registro dentro da tabela
    def post(self):
        cs = alimentos_schema.AlimentosSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            caloria = request.json["caloria"]
            proteina = request.json["proteina"]
            carboidrato = request.json["carboidrato"]
            gordura = request.json["gordura"]
            fibra = request.json["fibra"]
            grupo = request.json["grupo"]
            grama = request.json["grama"]
            colherSopaCheia = request.json["colherSopaCheia"]
            unidadeFatiaMedida = request.json["unidadeFatiaMedida"]
            mililitros = request.json["mililitros"]


            alimento_novo = alimentos.Alimentos(nome=nome,
                                                caloria=caloria,
                                                proteina=proteina,
                                                carboidrato=carboidrato,
                                                gordura=gordura,
                                                fibra=fibra,
                                                grupo=grupo,
                                                grama=grama,
                                                colherSopaCheia=colherSopaCheia,
                                                unidadeFatiaMedida=unidadeFatiaMedida,
                                                mililitros=mililitros)


            resultado = alimentos_service.cadastrar_alimento(alimento_novo)
            return make_response(cs.jsonify(resultado), 201)


class AlimentoDetail(Resource):
    def get(self, id):
        alimento = alimentos_service.listar_alimentos_id(id)
        if alimento is None:
            return make_response(jsonify("Alimento Não Encontrado"), 404)
        cs = alimentos_schema.AlimentosSchema()
        return make_response(cs.jsonify(alimento), 200)

    def put(self, id):
        alimento_bd = alimentos_service.listar_alimentos_id(id)
        if alimento_bd is None:
            return make_response(jsonify("Alimento Não Encontrado"), 404)
        cs = alimentos_schema.AlimentosSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            caloria = request.json["caloria"]
            proteina = request.json["proteina"]
            carboidrato = request.json["carboidrato"]
            gordura = request.json["gordura"]
            fibra = request.json["fibra"]
            grupo = request.json["grupo"]
            grama = request.json["grama"]
            colherSopaCheia = request.json["colherSopaCheia"]
            unidadeFatiaMedida = request.json["unidadeFatiaMedida"]
            mililitros = request.json["mililitros"]


            alimento_novo = alimentos.Alimentos(nome=nome,
                                                caloria=caloria,
                                                proteina=proteina,
                                                carboidrato=carboidrato,
                                                gordura=gordura,
                                                fibra=fibra,
                                                grupo=grupo,
                                                grama=grama,
                                                colherSopaCheia=colherSopaCheia,
                                                unidadeFatiaMedida=unidadeFatiaMedida,
                                                mililitros=mililitros)

            resultado = alimentos_service.atualizar_alimento(alimento_bd, alimento_novo)
            return make_response(cs.jsonify(resultado), 201)

    def delete(self, id):
        alimento = alimentos_service.listar_alimentos_id(id)
        if alimento is None:
            return make_response(jsonify("Alimento Não Encontrado"), 404)
        alimentos_service.exclui_alimento(alimento)
        return make_response(jsonify(""), 204)


api.add_resource(AlimentosList, '/alimentos')
api.add_resource(AlimentoDetail, '/alimentos/<int:id>')