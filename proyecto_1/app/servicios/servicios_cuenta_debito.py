from reglas.reglas import Validaciones
from modelo.cuenta_debito import Cuenta_Normal
from repositorios.repositorio_transacciones import Repositorio_Transacciones
from modelo.transacciones import Transacciones

class Servicio_Cuenta_Debito:
    def __init__(self, cuenta_normal:Cuenta_Normal, repositorio_transacciones: Repositorio_Transacciones):
        self.cuenta_normal=cuenta_normal
        self.rep_transacciones=repositorio_transacciones
        self.reglas=Validaciones()

    def consultar_saldo(self):
        self.cuenta_normal.consultar_saldo()
        id_tr="100"+str(len(self.rep_transacciones+1))

        transaccion=Transacciones(id_tr, "Cuenta de debito", "Consulta de saldo")
        self.rep_transacciones.agregar_transaccion(transaccion)

    def retirar(self, monto):
        saldo=self.cuenta_normal.consultar_saldo
        if self.reglas.no_exceder_limite(monto, saldo)==False:
            raise ValueError("Saldo insuficiente para realizar esta opreacion")
        self.cuenta_normal.retirar(monto)
        return 1


    def depositar(self, cantidad):
        self.cuenta_normal.depositar(cantidad)
        return 1