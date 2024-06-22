# Arquivo: entidades/receitas.py

class Receitas:
    def __init__(self, nome, caloria, proteina, carboidrato, gordura, fibra, grupo,
                 grama, colherSopa, unidadePedacoMedida, tempoPreparo, modo_preparo, imagem, alimentos):
        self.__nome = nome
        self.__caloria = caloria
        self.__proteina = proteina
        self.__carboidrato = carboidrato
        self.__gordura = gordura
        self.__fibra = fibra
        self.__grupo = grupo
        self.__grama = grama
        self.__colherSopa = colherSopa
        self.__unidadePedacoMedida = unidadePedacoMedida
        self.__tempoPreparo = tempoPreparo
        self.__modo_preparo = modo_preparo
        self.__imagem = imagem
        self.__alimentos = alimentos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def caloria(self):
        return self.__caloria

    @caloria.setter
    def caloria(self, caloria):
        self.__caloria = caloria

    @property
    def proteina(self):
        return self.__proteina

    @proteina.setter
    def proteina(self, proteina):
        self.__proteina = proteina

    @property
    def carboidrato(self):
        return self.__carboidrato

    @carboidrato.setter
    def carboidrato(self, carboidrato):
        self.__carboidrato = carboidrato

    @property
    def gordura(self):
        return self.__gordura

    @gordura.setter
    def gordura(self, gordura):
        self.__gordura = gordura

    @property
    def fibra(self):
        return self.__fibra

    @fibra.setter
    def fibra(self, fibra):
        self.__fibra = fibra

    @property
    def grupo(self):
        return self.__grupo

    @grupo.setter
    def grupo(self, grupo):
        self.__grupo = grupo

    @property
    def grama(self):
        return self.__grama

    @grama.setter
    def grama(self, grama):
        self.__grama = grama

    @property
    def colherSopa(self):
        return self.__colherSopa

    @colherSopa.setter
    def colherSopa(self, colherSopa):
        self.__colherSopa = colherSopa

    @property
    def unidadePedacoMedida(self):
        return self.__unidadePedacoMedida

    @unidadePedacoMedida.setter
    def unidadePedacoMedida(self, unidadePedacoMedida):
        self.__unidadePedacoMedida = unidadePedacoMedida

    @property
    def tempoPreparo(self):
        return self.__tempoPreparo

    @tempoPreparo.setter
    def tempoPreparo(self, tempoPreparo):
        self.__tempoPreparo = tempoPreparo

    @property
    def modo_preparo(self):
        return self.__modo_preparo

    @modo_preparo.setter
    def modo_preparo(self, modo_preparo):
        self.__modo_preparo = modo_preparo

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem

    @property
    def alimentos(self):
        return self.__alimentos

    @alimentos.setter
    def alimentos(self, alimentos):
        self.__alimentos = alimentos
