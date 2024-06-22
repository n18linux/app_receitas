class Alimentos():
    def __init__(self,
                 nome,
                 caloria,
                 proteina,
                 carboidrato,
                 gordura,
                 fibra,
                 grupo,
                 grama,
                 colherSopaCheia,
                 unidadeFatiaMedida,
                 mililitros
                 ):
        self.__nome = nome
        self.__caloria = caloria
        self.__proteina = proteina
        self.__carboidrato = carboidrato
        self.__gordura = gordura
        self.__fibra = fibra
        self.__grupo = grupo
        self.__grama = grama
        self.__colherSopaCheia = colherSopaCheia
        self.__unidadeFatiaMedida = unidadeFatiaMedida
        self.__mililitros = mililitros

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

#----------------------------------------------------------

    @property
    def caloria(self):
        return self.__caloria

    @caloria.setter
    def caloria(self, caloria):
        self.__caloria = caloria

#----------------------------------------------------------

    @property
    def proteina(self):
        return self.__proteina

    @proteina.setter
    def proteina(self, proteina):
        self.__proteina = proteina

#----------------------------------------------------------

    @property
    def carboidrato(self):
        return self.__carboidrato

    @carboidrato.setter
    def carboidrato(self, carboidrato):
        self.__carboidrato = carboidrato

#----------------------------------------------------------

    @property
    def gordura(self):
        return self.__gordura

    @gordura.setter
    def gordura(self, gordura):
        self.__gordura = gordura

#----------------------------------------------------------

    @property
    def fibra(self):
        return self.__fibra

    @fibra.setter
    def fibra(self, fibra):
        self.__fibra = fibra

#----------------------------------------------------------

    @property
    def grupo(self):
        return self.__grupo

    @grupo.setter
    def grupo(self, grupo):
        self.__grupo = grupo

#----------------------------------------------------------

    @property
    def grama(self):
        return self.__grama

    @grama.setter
    def grama(self, grama):
        self.__grama = grama

#----------------------------------------------------------

    @property
    def colherSopaCheia(self):
        return self.__colherSopaCheia

    @colherSopaCheia.setter
    def colherSopaCheia(self, colherSopaCheia):
        self.__colherSopaCheia = colherSopaCheia

#----------------------------------------------------------

    @property
    def unidadeFatiaMedida(self):
        return self.__unidadeFatiaMedida

    @unidadeFatiaMedida.setter
    def unidadeFatiaMedida(self, unidadeFatiaMedida):
        self.__unidadeFatiaMedida = unidadeFatiaMedida

#----------------------------------------------------------

    @property
    def mililitros(self):
        return self.__mililitros

    @mililitros.setter
    def mililitros(self, mililitros):
        self.__mililitros = mililitros