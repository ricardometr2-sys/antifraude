from modelo.cliente import Cliente
from repositorios.repositorio_transacciones import Repositorio_Transacciones
from repositorios.repositorio_cuentas import Repositorio_Cuentas
from modelo.cuenta_debito import Cuenta_Normal
from modelo.cuenta_debito import Cuenta_Ahorro
from modelo.cuenta_credito import Cuenta_Credito
from modelo.transacciones import Transacciones
from reglas.reglas import Validaciones

class Servicio_Cliente:
    def __init__(self, cliente: Cliente, rep_cuentas:Repositorio_Cuentas, rep_transacciones:Repositorio_Transacciones):
        self.cliente=cliente
        self.reptransacciones=rep_transacciones
        self.rep_cuentas=rep_cuentas
        self.reglas=Validaciones()


    #Editar perfil
    def editar_nombre(self, nuevo_nombre):
        self.cliente.nombre=nuevo_nombre

    def editar_contraseña(self, nueva_contraseña):
        self.cliente.contraseña=nueva_contraseña


    #Crear una cuenta
    def crear_cuenta_ahorro(self):
        if self.cliente._cuenta_ahorro==None:
            nombre_c=self.cliente.nombre
            cuenta_ah=Cuenta_Ahorro(nombre_c)
            self.cliente.crear_cuenta_ahorro(cuenta_ah)
            self.rep_cuentas.agregar_cuenta(cuenta_ah)

            id_tr="100"+str(len(self.rep_transacciones+1))
            transaccion=Transacciones(id_tr, "Cuenta prncipal", "Creaste una cuenta de ahorro")
            self.rep_transacciones.agregar_transaccion(transaccion)
        else:
            return 0

    def crear_cuenta_debito(self):
        if self.cliente._cuenta_debito==None:
            nombre_c=self.cliente.nombre
            cuenta_db=Cuenta_Normal(nombre_c)
            self.cliente.crear_cuenta_debito(cuenta_db)
            self.rep_cuentas.agregar_cuenta(cuenta_db)

            id_tr="100"+str(len(self.rep_transacciones+1))
            transaccion=Transacciones(id_tr, "Cuenta prncipal", "Creaste una cuenta de debito")
            self.rep_transacciones.agregar_transaccion(transaccion)
        else:
            return 0

    def crear_cuenta_credito(self):
        if self.cliente._cuenta_credito==None:
            nombre_c=self.cliente.nombre
            cuenta_cr=Cuenta_Credito(nombre_c)
            self.cliente.crear_cuenta_credito(cuenta_cr)
            self.rep_cuentas.agregar_cuenta(cuenta_cr)

            id_tr="100"+str(len(self.rep_transacciones+1))
            transaccion=Transacciones(id_tr, "Cuenta prncipal", "Creaste una cuenta de credito")
            self.rep_transacciones.agregar_transaccion(transaccion)
        else:
            return 0

    #Transacciones cuenta de debito
    def consultar_saldo_debito(self):
        self.cliente._cuenta_normal.consultar_saldo()
        id_tr="100"+str(len(self.rep_transacciones+1))

        transaccion=Transacciones(id_tr, "Cuenta de debito", "Consulta de saldo")
        self.rep_transacciones.agregar_transaccion(transaccion)

    def retirar_debito(self, monto):
        try:
            saldo=self.cliente._cuenta_normal.consultar_saldo()
            self.reglas.no_exceder_limite(monto, saldo)  
        except:
            return "No tienes saldo suficiente para realizar esta operacion"
        
        self.cliente._cuenta_normal.retirar(monto)
        id_tr="100"+str(len(self.rep_transacciones+1))
        transaccion=Transacciones(id_tr, "Cuenta de debito", "Retiro", monto)
        self.rep_transacciones.agregar_transaccion(transaccion)
        return 1

    def depositar_debito(self, monto):
        self.cliente._cuenta_normal.depositar(monto)

        id_tr="100"+str(len(self.rep_transacciones+1))
        transaccion=Transacciones(id_tr, "Cuenta de debito", "Deposito", monto)
        self.rep_transacciones.agregar_transaccion(transaccion)
        return 1

    #def transferencia_debito(self, monto, destino):
        #destino.depositar(monto)
        #self.retirar(monto)

    


    #Transacciones cuenta de ahorro
    def consultar_saldo_ahorro(self):
        self.cliente._cuenta_ahorro.consultar_saldo()
        id_tr="100"+str(len(self.rep_transacciones+1))

        transaccion=Transacciones(id_tr, "Cuenta de ahorro", "Consulta de saldo")
        self.rep_transacciones.agregar_transaccion(transaccion)

    def retirar_ahorro(self, monto):
        try:
            saldo=self.cliente._cuenta_ahorro.consultar_saldo()
            self.reglas.no_exceder_limite(monto, saldo)  
        except:
            return "No tienes saldo suficiente para realizar esta operacion"
        self.cliente._cuenta_ahorro.retirar(monto)
        self.cliente._cuenta_debito.depositar(monto)

        id_tr="100"+str(len(self.rep_transacciones+1))
        transaccion=Transacciones(id_tr, "Cuenta de ahorro", "Retiro", monto)
        self.rep_transacciones.agregar_transaccion(transaccion)
        return 1


    def depositar_ahorro(self, monto):
        if self.retirar_debito(monto)==1:
            self.cliente._cuenta_ahorro.retirar(monto)
        else:
            return 0
        
        id_tr="100"+str(len(self.rep_transacciones+1))
        transaccion=Transacciones(id_tr, "Cuenta de ahorro", "Deposito", monto)
        self.rep_transacciones.agregar_transaccion(transaccion)
        return 1


    #Transacciones cuenta de credito
    def compra_credito(self, monto):
        if self.cliente._cuenta_credito.pagar(monto):
            id_tr="100"+str(len(self.rep_transacciones+1))
            transaccion=Transacciones(id_tr, "Cuenta de credito", "Compra", monto)
            self.rep_transacciones.agregar_transaccion(transaccion)
            return 1
        return 0

    def ajustar_limite_credito(self, nuevo_limite):
        if self.cliente._cuenta_credito.ajustar_limite(nuevo_limite):
            id_tr="100"+str(len(self.rep_transacciones+1))
            transaccion=Transacciones(id_tr, "Cuenta de credito", "Ajuste de limite de credito")
            self.rep_transacciones.agregar_transaccion(transaccion)
            return 1
        return 0

    def pago_credito(self):
        saldo=self.consultar_saldo_debito()
        deuda=self.cliente._cuenta_credito.deuda
        if saldo>deuda:
            self.cliente._cuenta_credito.pagar_credito()

            id_tr="100"+str(len(self.rep_transacciones+1))
            transaccion=Transacciones(id_tr, "Cuenta de credito", "Pago de credito", deuda)
            self.rep_transacciones.agregar_transaccion(transaccion)            
            return 1
        return 0
    

    