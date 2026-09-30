from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, id_usuario, nombre, fecha_nacimiento, edad, codigo_postal, correo, contraseña):
        super().__init__(id_usuario, nombre, fecha_nacimiento, edad, codigo_postal, correo, contraseña)
        self.tipo_usario="Administrador"
        self.__llave_acceso=False

    def validar_acceso_administrador(self):
        self.__llave_acceso=True


        