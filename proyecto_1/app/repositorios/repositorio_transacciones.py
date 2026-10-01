class Repositorio_Transacciones:
    def __init__(self):
        self.rep_transacciones=list()

    def agregar_transaccion(self, transaccion):
            self.rep_transacciones.append(transaccion)

    def buscar_transaccion(self, id):
        if self.rep_transacciones:
            for trccn in self.rep_transacciones:
                if trccn._id_transaccion==id:
                    return trccn.GetTransaccion
        return False

    def mostrar_transacciones(self):
        if self.rep_transacciones:
            for tr in self.rep_transacciones:
                print(tr)
        return False

    def sum_tr(self):
        return int(len(self.rep_transacciones))