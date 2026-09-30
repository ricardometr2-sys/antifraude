from abc import ABC, abstractmethod

class Cuenta_Debito(ABC):
    def __init__(self, num_tarjeta, titular):
        self.__num_tarjeta=num_tarjeta
        self.titular=titular
        self.__año_vencimiento=0
        self.__cvc=0
        self._saldo=0
        
    def consultar_saldo(self):
        return self._saldo

    @abstractmethod
    def retirar(self, retiro)->bool:
        pass

    @abstractmethod
    def depositar(self, deposito)->bool:
        pass


class Cuenta_Normal(Cuenta_Debito):
    def __init__(self, num_tarjeta, titular):
        super().__init__(num_tarjeta, titular)

    def retirar(self, retiro):
        self._saldo-=retiro
        return

    def depositar(self, deposito):
        self._saldo+=deposito
        return

class Cuenta_Ahorro(Cuenta_Debito):
    def __init__(self, titular):
        super().__init__(titular)

    def retirar(self, retiro):
        self._saldo-=retiro
        return

    def depositar(self, deposito):
        self._saldo+=deposito
        return


