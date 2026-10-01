from app.modelo.cliente import Cliente
from app.repositorios.repositorio_transacciones import Repositorio_Transacciones
from app.repositorios.repositorio_cuentas import Repositorio_Cuentas
from app.modelo.cuenta_debito import Cuenta_Normal
from app.modelo.cuenta_debito import Cuenta_Ahorro
from app.modelo.cuenta_credito import Cuenta_Credito
from app.modelo.transacciones import Transacciones
from app.reglas.reglas import Validaciones

class Servicio_Cliente:
    def __init__(self, cliente: Cliente):
        self.cliente=cliente
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

            id_tr="100"+str((self.rep_transacciones.sum_tr()+1))
            transaccion=Transacciones(id_tr, "Cuenta prncipal", "Creaste una cuenta de ahorro")
            self.cliente.rep_transacciones.agregar_transaccion(transaccion)
        else:
            raise TypeError

    def crear_cuenta_debito(self):
        if self.cliente._cuenta_debito==None:
            nombre_c=self.cliente.nombre
            cuenta_db=Cuenta_Normal(nombre_c)
            self.cliente.crear_cuenta_debito(cuenta_db)
            id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)
            transaccion=Transacciones(id_tr, "Cuenta prncipal", "Creaste una cuenta de debito")
            self.cliente.rep_transacciones.agregar_transaccion(transaccion)
        else:
            raise TypeError

    def crear_cuenta_credito(self):
        if self.cliente._cuenta_credito==None:
            nombre_c=self.cliente.nombre
            cuenta_cr=Cuenta_Credito(nombre_c)
            self.cliente.crear_cuenta_credito(cuenta_cr)

            id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)
            transaccion=Transacciones(id_tr, "Cuenta prncipal", "Creaste una cuenta de credito")
            self.cliente.rep_transacciones.agregar_transaccion(transaccion)
        else:
            raise TypeError

    def validar_existancia_cuenta(self, cuenta):
        return True
    
    #Transacciones cuenta de debito
    def consultar_saldo_debito(self):
        if self.validar_existancia_cuenta(self.cliente._cuenta_debito):
            saldo= self.cliente._cuenta_debito.consultar_saldo()
            id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)

            transaccion=Transacciones(id_tr, "Cuenta de debito", "Consulta de saldo")
            self.cliente.rep_transacciones.agregar_transaccion(transaccion)
            return saldo
        raise TypeError

    def retirar_debito(self, monto):
        if self.validar_existancia_cuenta(self.cliente._cuenta_debito):
            saldo=self.cliente._cuenta_debito.consultar_saldo()
            self.reglas.no_exceder_limite(monto, saldo)  
            
            
            self.cliente._cuenta_debito.retirar(monto)
            id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)
            transaccion=Transacciones(id_tr, "Cuenta de debito", "Retiro", monto)
            self.cliente.rep_transacciones.agregar_transaccion(transaccion)
            return 1
        raise TypeError

    def depositar_debito(self, monto):
        if self.validar_existancia_cuenta(self.cliente._cuenta_debito):
            self.cliente._cuenta_debito.depositar(monto)

            id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)
            transaccion=Transacciones(id_tr, "Cuenta de debito", "Deposito", monto)
            self.cliente.rep_transacciones.agregar_transaccion(transaccion)
            return 1
        raise TypeError

    #def transferencia_debito(self, monto, destino):
        #destino.depositar(monto)
        #self.retirar(monto)

    


    #Transacciones cuenta de ahorro
    def consultar_saldo_ahorro(self):
        if self.validar_existancia_cuenta(self.cliente._cuenta_ahorro):
            saldo= self.cliente._cuenta_ahorro.consultar_saldo()
            id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)

            transaccion=Transacciones(id_tr, "Cuenta de ahorro", "Consulta de saldo")
            self.cliente.rep_transacciones.agregar_transaccion(transaccion)
            return saldo
        raise TypeError

    def retirar_ahorro(self, monto):
        if self.validar_existancia_cuenta(self.cliente._cuenta_ahorro):
            saldo=self.cliente._cuenta_ahorro.consultar_saldo()
            self.reglas.no_exceder_limite(monto, saldo)  
            
            self.cliente._cuenta_ahorro.retirar(monto)
            self.cliente._cuenta_debito.depositar(monto)

            id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)
            transaccion=Transacciones(id_tr, "Cuenta de ahorro", "Retiro", monto)
            self.cliente.rep_transacciones.agregar_transaccion(transaccion)
            return 1
        raise TypeError


    def depositar_ahorro(self, monto):
        if self.validar_existancia_cuenta(self.cliente._cuenta_ahorro):
            if self.retirar_debito(monto)==1:
                self.cliente._cuenta_ahorro.retirar(monto)
            else:
                return 0
            
            id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)
            transaccion=Transacciones(id_tr, "Cuenta de ahorro", "Deposito", monto)
            self.cliente.rep_transacciones.agregar_transaccion(transaccion)
            return 1
        raise TypeError

    #Transacciones cuenta de credito
    def compra_credito(self, monto):
        if self.validar_existancia_cuenta(self.cliente._cuenta_credito):
            if self.cliente._cuenta_credito.pagar(monto):
                id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)
                transaccion=Transacciones(id_tr, "Cuenta de credito", "Compra", monto)
                self.cliente.rep_transacciones.agregar_transaccion(transaccion)
                return 1
            raise 
        raise TypeError

    def ajustar_limite_credito(self, nuevo_limite):
        if self.validar_existancia_cuenta(self.cliente._cuenta_ahorro):
            if self.cliente._cuenta_credito.ajustar_limite(nuevo_limite):
                id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)
                transaccion=Transacciones(id_tr, "Cuenta de credito", "Ajuste de limite de credito")
                self.cliente.rep_transacciones.agregar_transaccion(transaccion)
                return 1
            return 0
        raise TypeError

    def consultar_credito(self):
        if self.validar_existancia_cuenta(self.cliente._cuenta_ahorro):
            credito=self.cliente._cuenta_credito.credito
            deuda=self.cliente._cuenta_credito.deuda
            return f"Credito: {credito}, Fatan por pagar: {deuda}"
        raise ValueError


    def pago_credito(self):
        if self.validar_existancia_cuenta(self.cliente._cuenta_ahorro):
            saldo=self.consultar_saldo_debito()
            deuda=self.cliente._cuenta_credito.deuda
            if saldo>deuda:
                self.retirar_debito(deuda)
                self.cliente._cuenta_credito.pagar_credito()

                id_tr="100"+str((self.cliente.rep_transacciones.sum_tr())+1)
                transaccion=Transacciones(id_tr, "Cuenta de credito", "Pago de credito", deuda)
                self.cliente.rep_transacciones.agregar_transaccion(transaccion)            
                return 1
            return 0
        raise TypeError
    

    