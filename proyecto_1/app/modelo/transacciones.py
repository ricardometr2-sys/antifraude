from datetime import datetime 

class Transacciones:
    def __init__(self, id_transaccion, usuario, cuenta, tipo, monto):
        self._id_transaccion=id_transaccion
        self._usuario=usuario
        self.tipo=tipo
        self.cuenta=cuenta
        self.monto=monto
        self.fecha_transaccion=datetime.now().strftime("Y:m:D a las H:M horas")
    
    def GetTransaccion(self):
        trccion={
            "ID": self._id_transaccion,
            "Usario": self._usuario,
            "Cuenta": self.cuenta,
            "Tipo": self.tipo,
            "Monto": self.monto
        }
        return trccion

    def __str__(self):
        trccion={
            "ID": self._id_transaccion,
            "Usario": self._usuario,
            "Cuenta": self.cuenta,
            "Tipo": self.tipo,
            "Monto": self.monto
        }
        return trccion