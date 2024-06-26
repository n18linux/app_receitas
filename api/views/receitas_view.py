from flask_restful import Resource
from ..schemas import receitas_schema
from flask import request, make_response, jsonify
from ..entidades import receitas
from ..services import receitas_service, alimentos_service
from api import api

class ReceitasList(Resource):


    def get(self):
        try:
            receitas = receitas_service.listar_receitas()
            re = receitas_schema.ReceitaSchema(many=True)
            return make_response(re.jsonify(receitas), 200)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)



    def post(self):
        re = receitas_schema.ReceitaSchema()
        try:
            validate = re.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                _nome = request.json["nome"]
                _caloria = request.json["caloria"]
                _proteina = request.json["proteina"]
                _alimentos_id = request.json["alimentos_id"]

                # Verifico se o ID do alimento existe na tb_alimento
                if alimentos_service.listar_alimento_id(_alimentos_id) is None:
                    return make_response("Alimento não existe", 404)
                else:
                    receita_nova = receitas.Receitas(nome=_nome,
                                                     caloria=_caloria,
                                                     proteina=_proteina,
                                                     alimentos_id=_alimentos_id)

                resultado = receitas_service.cadastrar_receita(receita_nova)
                return make_response(re.jsonify(resultado), 201)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


class ReceitasDetail(Resource):

    def get(self, id):
        try:
            receitas = receitas_service.listar_receita_id(id)
            if not receitas:
                return make_response(jsonify({"error": "Receita não encontrada"}), 404)
            re = receitas_schema.ReceitaSchema()
            return make_response(re.jsonify(receitas), 200)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


    def put(self, id):
        try:
            receita_bd = receitas_service.listar_receita_id(id)
            if not receita_bd:
                return make_response(jsonify({"error": "Receita não encontrada"}), 404)

            re = receitas_schema.ReceitaSchema()
            validate = re.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                _nome = request.json["nome"]
                _caloria = request.json["caloria"]
                _proteina = request.json["proteina"]
                _alimentos_id = request.json["alimentos_id"]

                # Verifico se o ID do alimento existe na tb_alimento
                if alimentos_service.listar_alimento_id(_alimentos_id) is None:
                    return make_response("Alimento não existe", 404)
                else:
                    receita_nova = receitas.Receitas(nome=_nome,
                                                     caloria=_caloria,
                                                     proteina=_proteina,
                                                     alimentos_id=_alimentos_id)

                resultado = receitas_service.atualizar_receita(receita_bd, receita_nova)
                return make_response(re.jsonify(resultado), 201)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


    def delete(self, id):
        try:
            receita = receitas_service.listar_receita_id(id)
            if not receita:
                return make_response(jsonify({"error": "Receita não encontrada"}), 404)

            receitas_service.exclui_receita(receita)
            return make_response(jsonify({"message": "Receitao excluída com sucesso"}), 204)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

api.add_resource(ReceitasList,'/receita')
api.add_resource(ReceitasDetail,'/receita/<int:id>')
