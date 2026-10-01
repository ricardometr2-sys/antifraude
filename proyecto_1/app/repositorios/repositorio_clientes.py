class Repositorio_Clientes:
    def __init__(self):
        self._rep_clientes=list()

    def agregar_usuario(self, usuario):
        self._rep_clientes.append(usuario)

    def dar_primer_usuario(self):
        return self._rep_clientes[0]

    def buscar_usuario(self, correo):
        if self._rep_clientes:
            for usuario in self._rep_clientes:
                if usuario.correo_electronico==correo:
                    return usuario     
            return usuario      
        else:
            raise ValueError

    def obtener_clientes(self, tipo):
        if self._rep_clientes:
            return self._rep_clientes
        else:
            raise ValueError
            