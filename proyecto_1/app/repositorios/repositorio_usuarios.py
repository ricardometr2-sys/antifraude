class Repositorio_Usirios:
    def __init__(self):
        self.rep_usuarios=list()

    def agregar_usuario(self, usuario):
        self.rep_usuarios.append(usuario)

    def buscar_usario(self, id_usuario):
        if self.rep_usuarios:
            for us in self.rep_usuarios:
                usuario=us.__id_usuario
                if usuario==id_usuario:
                    return us
            return False
        return False

    def obtener_clientes(self):
        if self.rep_usuarios:
            return self.rep_usuarios
        return False

    