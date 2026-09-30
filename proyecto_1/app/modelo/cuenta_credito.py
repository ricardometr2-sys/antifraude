class Cuenta_Credito:
    def __init__(self, num_cuenta, titular):
        self.__num_cuenta=num_cuenta
        self._titular=titular
        self._limite_credito=0

    def ajustar_limite(self,nuevo_limite):
        self._limite_credito=nuevo_limite
        return 1

