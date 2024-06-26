class Refeicao:
    def __init__(self,
                 nome,
                 horario,
                 idDietaPronta,
                 idReceita,
                 idAlimento
                 ):
        self.__nome = nome
        self.__horario = horario
        self.__idDietaPronta = idDietaPronta
        self.__aidReceita = idReceita
        self.__idAlimento = idAlimento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # ----------------------------------------------------------

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    # ----------------------------------------------------------
    @property
    def idDietaPronta(self):
        return self.__idDietaPronta

    @idDietaPronta.setter
    def idDietaPronta(self, idDietaPronta):
        self.__idDietaPronta = idDietaPronta

    # ----------------------------------------------------------

    @property
    def idReceita(self):
        return self.__idReceita

    @idReceita.setter
    def idReceita(self, idReceita):
        self.__idReceita = idReceita

    # ----------------------------------------------------------

    @property
    def idAlimento(self):
        return self.__idAlimento

    @idAlimento.setter
    def idAlimento(self, idAlimento):
        self.__idAlimento = idAlimento

    # ----------------------------------------------------------