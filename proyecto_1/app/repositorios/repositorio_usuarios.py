class Repositorio_Usirios:
    def __init__(self):
        self.rep_clientes=list()
        self.rep_administradores=list()

    def agregar_usuario(self, usuario, tipo):
        if tipo==1:
            self.rep_usuarios.append(usuario)
        elif tipo ==2:
            self.rep_administradores.append(usuario)

    def buscar_usario(self, id_usuario, tipo):
        if tipo==1:
            if self.rep_usuarios:
                for us in self.rep_usuarios:
                    usuario=us.__id_usuario
                    if usuario==id_usuario:
                        return us
                return False
        elif tipo==2:
            if self.rep_administradores:
                for us in self.rep_administradores:
                    usuario=us.__id_usuario
                    if usuario==id_usuario:
                        return us
                return False
        return False

    def obtener_clientes(self, tipo):
        if tipo==1:
            if self.rep_usuarios:
                return self.rep_usuarios
        elif tipo==2:
            if self.rep_administradores:
                return self.rep_administradores
        return False

    