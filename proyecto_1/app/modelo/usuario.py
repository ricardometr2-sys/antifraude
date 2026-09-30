class Usuario:
    def __init__(self, id_usuario, nombre, fecha_nacimiento, codigo_postal, correo, contraseña):
        self.__id_usuario=id_usuario
        self.__nombre=nombre
        self.__fecha_lanzamiento=fecha_nacimiento
        self.__codigo_postal=codigo_postal
        self.__correo_electronico=correo
        self.__contraseña=contraseña

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, n_nombre):
        self.__nombre=n_nombre

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
            "Fecha de nacimiento": self.__fecha_lanzamiento,
            "Codigo postal": self.__codigo_postal,
        }
        return datos



    