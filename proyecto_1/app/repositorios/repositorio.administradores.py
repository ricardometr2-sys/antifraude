class Repositorio_Administradores:
    def __init__(self):
        self._rep_administradores=list()
        
        def agregar_admin(self, usuario):
            self._rep_administradores.append(usuario)
    
        def buscar_admin(self, id_usuario):
            if self._rep_administradores:
                for us in self._rep_administradores:
                    if us.id_usuario==id_usuario:
                        return us
            raise ValueError
    
        def obtener_admins(self, tipo):
            if self._rep_administradores:
                return self._rep_administradores
            else:
                raise ValueError