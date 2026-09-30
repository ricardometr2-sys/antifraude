from reglas.reglas import Validaciones
from modelo.cliente import Cliente


class Servicio_Cliente:
    def __init__(self, cliente: Cliente):
        self.cliente=cliente

    def entrar_cuenta_debito(self):
        return self.cliente.__cuenta_debito

    def entrar_cuenta_ahorro(self):
        return self.cliente.__cuenta_ahorro

    def entrar_cuenta_debito(self):
        return self.cliente.__cuenta_credito

print("jf dk")
    

    