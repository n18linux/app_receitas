from flask_restful import Resource
from ..schemas import refeicao_schema
from flask import request, make_response, jsonify
from ..entidades import refeicao
from ..services import refeicao_service
from api import api

class RefeicoesList(Resource):


    def get(self):
        try:
            refeicoes = refeicao_service.listar_refeicoes()
            re = refeicao_schema.RefeicaoSchema(many=True)
            return make_response(re.jsonify(refeicoes), 200)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)



    def post(self):
        re = refeicao_schema.RefeicaoSchema()
        try:
            validate = re.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                dados_refeicao = request.json
                refeicao_nova = refeicao.Refeicao(nome=dados_refeicao["nome"],
                                                    horario=dados_refeicao["horario"],
                                                    idDietaPronta=dados_refeicao["idDietaPronta"],
                                                    idReceita=dados_refeicao["idReceita"],
                                                    idAlimento=dados_refeicao["idAlimento"])

                resultado = refeicao_service.cadastrar_refeicao(refeicao_nova)
                return make_response(re.jsonify(resultado), 201)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


class RefeicoesDetail(Resource):

    def get(self, id):
        try:
            refeicao = refeicao_service.listar_refeicoes_id(id)
            if not refeicao:
                return make_response(jsonify({"error": "Refeição não encontrada"}), 404)
            re = refeicao_schema.RefeicaoSchema()
            return make_response(re.jsonify(refeicao), 200)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


    def put(self, id):
        try:
            refeicao_bd = refeicao_service.listar_refeicoes_id(id)
            if not refeicao_bd:
                return make_response(jsonify({"error": "Refeição não encontrada"}), 404)

            re = refeicao_schema.RefeicaoSchema()
            validate = re.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                dados_refeicao = request.json
                refeicao_nova = refeicao.Refeicao(nome=dados_refeicao["nome"],
                                                  horario=dados_refeicao["horario"],
                                                  idDietaPronta=dados_refeicao["idDietaPronta"],
                                                  idReceita=dados_refeicao["idReceita"],
                                                  idAlimento=dados_refeicao["idAlimento"])


                resultado = refeicao_service.atualizar_refeicao(refeicao_bd, refeicao_nova)
                return make_response(re.jsonify(resultado), 201)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


    def delete(self, id):
        try:
            refeicao = refeicao_service.listar_refeicoes_id(id)
            if not refeicao:
                return make_response(jsonify({"error": "Refeição não encontrada"}), 404)

            refeicao_service.exclui_refeicao(refeicao)
            return make_response(jsonify({"message": "Refeição excluída com sucesso"}), 204)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

api.add_resource(RefeicoesList, '/refeicao')
api.add_resource(RefeicoesDetail, '/refeicao/<int:id>')
