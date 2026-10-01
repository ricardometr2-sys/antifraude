class Validaciones:
    def __init__(self):
        pass

    def validar_cadena_vacia(self, cadena)->bool:
        if len(str(cadena))<=3:
            raise TypeError
        else:
            return 1
        

    def no_exceder_limite(self, disponible, limite)->bool:
        if disponible>limite:
            raise SyntaxError
        return 1


class SaldoInsuficienteError(Exception):
    pass
        