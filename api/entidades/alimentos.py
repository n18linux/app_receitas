class Alimentos():
    def __init__(self,
                 nome,
                 caloria,
                 proteina
                 ):
        self.__nome = nome
        self.__caloria = caloria
        self.__proteina = proteina


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