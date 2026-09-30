class Validaciones:
    def __init__(self):
        pass

    def validar_cadena_vacia(self, cadena)->bool:
        if len(str(cadena))==0:
            raise ValueError("La cadena no puedes estar vacia") 
        return 1

    def no_exceder_limite(self, disponible, limite)->bool:
        if disponible>limite:
            raise SyntaxError("No tienes saldo suficiente") 
        return 1

    def validar_contraseña(self, cont):
        self.validar_cadena_vacia(cont)
        