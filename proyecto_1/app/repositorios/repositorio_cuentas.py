class Repositorio_Cuentas:
    def __init__(self):
        self._rep_cuentas=list()

    def agregar_cuenta(self, cuenta):
        self._rep_cuentas.append(cuenta)

    def obtener_cuenta(self, tipo):
        for cuenta in self._rep_cuentas:
            if cuenta.tipo==tipo:
                return cuenta
        return 1


        