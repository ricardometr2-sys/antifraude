from app.servicios.servicios_banco import Servicios_Banco
from app.servicios.servicios_administrador import Servicios_Administrador
from app.servicios.servicios_cliente import Servicio_Cliente
from app.repositorios.repositorio_clientes import Repositorio_Clientes
from app.repositorios.repositorio_transacciones import Repositorio_Transacciones
from app.modelo.usuario import Usuario


usuarios_rep=Repositorio_Clientes()
banco=Servicios_Banco(usuarios_rep)

banco.registrar_cliente("12432", "PEPE", "12/07/02", 51355, "changotremendo@noce.o", "pepe1123")
banco.registrar_cliente("12433", "Juan", "09/25/99", 53551, "sidnfnf@noce.o", "juan123")
cliente1=banco.inicio_sesion("changotremendo@noce.o")
cliente2=banco.inicio_sesion("12433")

#Cliente 1
servicio_cliente1=Servicio_Cliente(cliente1)
servicio_cliente1.crear_cuenta_debito()
servicio_cliente1.depositar_debito(1000)
servicio_cliente1.consultar_saldo_debito()
servicio_cliente1.retirar_debito(40)
print(servicio_cliente1.consultar_saldo_debito())

servicio_cliente1.crear_cuenta_credito()
servicio_cliente1.compra_credito(300)
print(servicio_cliente1.consultar_credito())
servicio_cliente1.pago_credito()
print(servicio_cliente1.consultar_saldo_debito())

#Cliente 2
ser_cliente2=Servicio_Cliente(cliente2)
ser_cliente2.crear_cuenta_credito()
ser_cliente2.crear_cuenta_debito()
print(ser_cliente2.consultar_credito())
ser_cliente2.depositar_debito(1000)

    





