class Usuario:
    def __init__(self, id_usuario, nombre, fecha_nacimiento, edad, codigo_postal, numero_telefono):
        self.id_usuario=id_usuario
        self._nombre=nombre
        self._fecha_lanzamiento=fecha_nacimiento
        self._edad=edad
        self._codigo_postal=codigo_postal
        self._num_telefono=numero_telefono
        self.__cuenta_debito=None
        self.__cuenta_credito=None
        self.__cuenta_ahorro=None

    def crear_cuenta_debito(self, cuenta:object):
        self.__cuenta_debito=cuenta

    def crear_cuenta_debito(self, cuenta:object):
        self.__cuenta_credito=cuenta

    def crear_cuenta_debito(self, cuenta:object):
        self.__cuenta_ahorro=cuenta

        
    