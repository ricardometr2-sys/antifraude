import random

class Cuenta_Credito:
    def __init__(self, titular):
        self.tipo="CR"
        self.__num_tarjeta="3"+str(random.randint(1110,9999))+"5"+str((random.randint(10,99)))
        self.__nip=random.randint(100, 999)
        self._titular=titular
        self.__limite_credito=1000
        self.__credito=1000
        self.__deuda=0

    def ajustar_limite(self,nuevo_limite):
        if nuevo_limite>self.__limite_credito:
            return 0
        self.__limite_credito=nuevo_limite
        return 1

    def pagar(self, cantidad):
        if cantidad>self.__credito:
            return 0
        self.__credito-=cantidad
        self.__deuda+=cantidad
        return 1

    def pagar_credito(self):
        self.__credito=self.__limite_credito
        self.__deuda=0

    @property
    def credito(self):
        return self.__credito

    @property
    def deuda(self):
        return self.__deuda

    @property
    def nip(self):
        return self.__nip

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta
    

