class Repositorio_Usuarios:
    def __init__(self):
        self._rep_clientes = list()
        self._rep_administradores = list()

    def agregar_usuario(self, usuario):
        if usuario.__id_usuario(0) == "C":
            self._rep_clientes.append(usuario)
        elif usuario.__id_usuario(0) == "A":
            self._rep_administradores.append(usuario)

    def buscar_usuario(self, id_usuario):
        if id_usuario(0) == "C":
            if self._rep_clientes:
                for us in self._rep_clientes:
                    if us.__id_usuario == id_usuario:
                        return us
        elif id_usuario(0) == "A":
            if self._rep_administradores:
                for us in self._rep_administradores:
                    if us.__id_usuario == id_usuario:
                        return us
        raise ValueError("ID de usuario no encontrado")

    def obtener_clientes(self, tipo):
        if tipo.__id == 1:
            if self._rep_clientes:
                return self._rep_clientes
        elif tipo == 2:
            if self._rep_administradores:
                return self._rep_administradores
        else:
            if tipo != 1 and tipo != 2:
                raise ValueError("Tipo de usuario no encontrado")
            

    