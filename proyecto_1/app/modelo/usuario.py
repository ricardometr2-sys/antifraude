class Usuario:
    def __init__(self, id_usuario, nombre, correo, fecha_nacimiento, codigo_postal, contraseña, rep_transacciones):
        self.__id_usuario=id_usuario
        self.__nombre=nombre
        self.__fecha_lanzamiento=fecha_nacimiento
        self.__codigo_postal=codigo_postal
        self.__correo_electronico=str(correo)
        self.__contraseña=contraseña
        self.rep_transacciones=rep_transacciones

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, n_nombre):
        self.__nombre=n_nombre

    @property
    def correo_electronico(self):
        return self.__correo_electronico

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, n_contraseña):
        self.__contraseña=n_contraseña

    def getDatos_usuario(self):
        datos={
            "ID": self.__id_usuario,
            "Nombre": self.__nombre,
            "Correo electronico": self.correo_electronico,
            "Fecha de nacimiento": self.__fecha_lanzamiento,
            "Codigo postal": self.__codigo_postal,
        }
        return datos



    