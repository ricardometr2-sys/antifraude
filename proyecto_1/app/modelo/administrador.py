from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, id_usuario, nombre, correo, fecha_nacimiento, codigo_postal, contraseña):
        super().__init__(id_usuario, nombre,correo,  fecha_nacimiento, codigo_postal, contraseña)
        self.__id_usuario="A"+str(id_usuario)
        self.tipo_usario="Administrador"
        self.__llave_acceso=False

    def validar_acceso_administrador(self):
        self.__llave_acceso=True


        