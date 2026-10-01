from usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id_usuario, nombre, correo, fecha_nacimiento, codigo_postal, contraseña):
        super().__init__(id_usuario, nombre, correo,  fecha_nacimiento, codigo_postal, correo, contraseña)
        self.__id_usuario="C"+str(id_usuario)
        self.tipo_usuario="Cliente"
        self._cuenta_debito=None
        self._cuenta_credito=None
        self._cuenta_ahorro=None

    def crear_cuenta_debito(self, cuenta:object):
        self._cuenta_debito=cuenta

    def crear_cuenta_credito(self, cuenta:object):
        self._cuenta_credito=cuenta

    def crear_cuenta_ahorro(self, cuenta:object):
        self._cuenta_ahorro=cuenta
