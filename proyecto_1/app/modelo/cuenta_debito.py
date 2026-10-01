from abc import ABC, abstractmethod
import random

class Cuenta_Debito(ABC):
    def __init__(self, titular):
        self.tipo=""
        self.titular=titular
        self._saldo = 0
        
    @abstractmethod
    def consultar_saldo(self):
        pass

    @abstractmethod
    def retirar(self, retiro)->bool:
        pass

    @abstractmethod
    def depositar(self, deposito)->bool:
        pass


class Cuenta_Normal(Cuenta_Debito):
    def __init__(self, titular):
        super().__init__(titular)
        self.tipo="DN"
        self.__num_tarjeta=self.__num_tarjeta="3"+str(random.randint(1110,9999))+"5"+str((random.randint(10,99)))
        self.__nip=random.randint(1,999)
        self.__año_vencimiento=0
        self.__cvc=0
        self.__saldo=0

    def consultar_saldo(self):
        return self.__saldo

    def retirar(self, retiro):
        self._saldo-=retiro
        return True

    def depositar(self, deposito):
        self._saldo+=deposito
        return True

    @property
    def nip(self):
        return self.__nip

class Cuenta_Ahorro(Cuenta_Debito):
    def __init__(self, titular):
        super().__init__(titular)
        self._saldo=0
        self.tipo="AH"

    def consultar_saldo(self):
        return self.__saldo

    def retirar(self, retiro):
        self._saldo-=retiro
        return True

    def depositar(self, deposito):
        self._saldo+=deposito
        return True


