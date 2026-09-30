from usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id_usuario, nombre, fecha_nacimiento, edad, codigo_postal, correo, contraseña):
        super().__init__(id_usuario, nombre, fecha_nacimiento, edad, codigo_postal, correo, contraseña)
        self.__id_usuario="C"+str(id_usuario)
        self.tipo_usuario="Cliente"
        self.__cuenta_debito=None
        self.__cuenta_credito=None
        self.__cuenta_ahorro=None

    def crear_cuenta_debito(self, cuenta:object):
        self.__cuenta_debito=cuenta

    def crear_cuenta_debito(self, cuenta:object):
        self.__cuenta_credito=cuenta

    def crear_cuenta_debito(self, cuenta:object):
        self.__cuenta_ahorro=cuenta
