from app.modelo.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, id_usuario, nombre, correo, fecha_nacimiento, codigo_postal, contraseña, rep_transacciones):
        super().__init__(id_usuario, nombre,correo,  fecha_nacimiento, codigo_postal, contraseña, rep_transacciones)
        self.__id_usuario="A"+str(id_usuario)
        self.tipo_usario="Administrador"
        self.__llave_acceso=False
    @property
    def id_usuario(self):
        return self.__id_usuario

    def validar_acceso_administrador(self):
        self.__llave_acceso=True


        