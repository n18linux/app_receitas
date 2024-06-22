from flask_restful import Resource
from ..schemas import receitas_schema
from flask import request, make_response, jsonify
from ..entidades import receitas
from ..services import receitas_service
from api import api


class ReceitasList(Resource):

    # Mostra toda as informações dentro da tebela
    def get(self):
        receita = receitas_service.listar_receitas()
        cs = receitas_schema.ReceitasSchema(many=True)
        return make_response(cs.jsonify(receitas), 201)

    # Cria um novo registro dentro da tabela
    def post(self):
        cs = receitas_schema.ReceitasSchema()
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
            colherSopa = request.json["colherSopa"]
            unidadeFatiaMedida = request.json["unidadeFatiaMedida"]
            tempoPreparo = request.json["tempoPreparo"]
            modo_preparo = request.json["modo_preparo"]
            imagem = request.json["imagem"]
            alimentos = request.json["alimentos"]


            receita_novo = receitas.Receitas(nome=nome,
                                                caloria=caloria,
                                                proteina=proteina,
                                                carboidrato=carboidrato,
                                                gordura=gordura,
                                                fibra=fibra,
                                                grupo=grupo,
                                                grama=grama,
                                                colherSopa=colherSopa,
                                                unidadeFatiaMedida=unidadeFatiaMedida,
                                                tempoPreparo=tempoPreparo,
                                                modo_preparo=modo_preparo,
                                                imagem=imagem,
                                                alimentos=alimentos)


            resultado = receitas_service.cadastrar_receita(receita_novo)
            return make_response(cs.jsonify(resultado), 201)


class ReceitasDetail(Resource):
    def get(self, id):
        receita = receitas_service.listar_receitas_id(id)
        if receita is None:
            return make_response(jsonify("Receita Não Encontrado"), 404)
        cs = receitas_schema.ReceitasSchema()
        return make_response(cs.jsonify(receita), 200)

    def put(self, id):
        receita_bd = receitas_service.listar_receitas_id(id)
        if receita_bd is None:
            return make_response(jsonify("Receita Não Encontrado"), 404)
        cs = receitas_schema.ReceitasSchema()
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
            colherSopa = request.json["colherSopa"]
            unidadeFatiaMedida = request.json["unidadeFatiaMedida"]
            tempoPreparo = request.json["tempoPreparo"]
            modo_preparo = request.json["modo_preparo"]
            imagem = request.json["imagem"]
            alimentos = request.json["alimentos"]

            receita_novo = receitas.Receitas(nome=nome,
                                             caloria=caloria,
                                             proteina=proteina,
                                             carboidrato=carboidrato,
                                             gordura=gordura,
                                             fibra=fibra,
                                             grupo=grupo,
                                             grama=grama,
                                             colherSopa=colherSopa,
                                             unidadeFatiaMedida=unidadeFatiaMedida,
                                             tempoPreparo=tempoPreparo,
                                             modo_preparo=modo_preparo,
                                             imagem=imagem,
                                             alimentos=alimentos)

            resultado = receitas_service.atualizar_receita(receita_bd, receita_novo)
            return make_response(cs.jsonify(resultado), 201)

    def delete(self, id):
        receita = receitas_service.listar_receitas_id(id)
        if receita is None:
            return make_response(jsonify("Receita Não Encontrado"), 404)
        receitas_service.excluir_receita(receita)
        return make_response(jsonify(""), 204)


api.add_resource(ReceitasList, '/receitas')
api.add_resource(ReceitasDetail, '/receitas/<int:id>')