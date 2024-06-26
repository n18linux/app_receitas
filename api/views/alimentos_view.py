from flask_restful import Resource
from ..schemas import alimentos_schema
from flask import request, make_response, jsonify
from ..entidades import alimentos
from ..services import alimentos_service
from api import api

class AlimentosList(Resource):


    def get(self):
        try:
            alimentos = alimentos_service.listar_alimentos()
            al = alimentos_schema.AlimentoSchema(many=True)
            return make_response(al.jsonify(alimentos), 200)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)



    def post(self):
        al = alimentos_schema.AlimentoSchema()
        try:
            validate = al.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                dados_alimento = request.json

                alimento_novo = alimentos.Alimentos(nome=dados_alimento["nome"],
                                                    caloria=dados_alimento["caloria"],
                                                    proteina=dados_alimento["proteina"])

                resultado = alimentos_service.cadastrar_alimento(alimento_novo)
                return make_response(al.jsonify(resultado), 201)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


class AlimentosDetail(Resource):

    def get(self, id):
        try:
            alimento = alimentos_service.listar_alimento_id(id)
            if not alimento:
                return make_response(jsonify({"error": "Alimento não encontrado"}), 404)
            al = alimentos_schema.AlimentoSchema()
            return make_response(al.jsonify(alimento), 200)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


    def put(self, id):
        try:
            alimento_bd = alimentos_service.listar_alimento_id(id)
            if not alimento_bd:
                return make_response(jsonify({"error": "Alimento não encontrado"}), 404)

            al = alimentos_schema.AlimentoSchema()
            validate = al.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                dados_alimento = request.json
                alimento_novo = alimentos.Alimentos(nome=dados_alimento["nome"],
                                                    caloria=dados_alimento["caloria"],
                                                    proteina=dados_alimento["proteina"])


                resultado = alimentos_service.atualizar_alimento(alimento_bd, alimento_novo)
                return make_response(al.jsonify(resultado), 201)


        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


    def delete(self, id):
        try:
            alimento = alimentos_service.listar_alimento_id(id)
            if not alimento:
                return make_response(jsonify({"error": "Alimento não encontrado"}), 404)

            alimentos_service.exclui_alimento(alimento)
            return make_response(jsonify({"message": "Alimento excluído com sucesso"}), 204)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

api.add_resource(AlimentosList, '/alimento')
api.add_resource(AlimentosDetail, '/alimento/<int:id>')
