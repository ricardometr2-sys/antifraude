import random

class Cuenta_Credito:
    def __init__(self, titular):
        self.tipo="CR"
        self.__num_tarjeta="3"+str(random.randint(1110,9999))+"5"+str((random.randint(10,99)))
        self.__nip=random.randint(100, 999)
        self._titular=titular
        self._limite_credito=1000
        self._credito=1000
        self._deuda=0

    def ajustar_limite(self,nuevo_limite):
        if nuevo_limite>self._limite_credito:
            return 0
        self._limite_credito=nuevo_limite
        return 1

    def pagar(self, cantidad):
        if cantidad>self._credito:
            return 0
        self._credito-=cantidad
        self._deuda+=cantidad
        return 1

    def pagar_credito(self):
        self._credito=self._limite_credito
        self._deuda=0

    @property
    def nip(self):
        return self.__nip

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta
    

