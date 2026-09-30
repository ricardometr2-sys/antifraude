import string

class Validaciones:
    def __init__(self):
        pass

    def validar_cadena_vacia(cadena)->bool:
        while True:
            try:
                if len(str(cadena))==0:
                    raise Exception            
                break
            except:
                print("La cadena no puede estar vacia")

    def no_exceder_limite(cantidad, limite)->bool:      
        if cantidad<limite:
            return 1
        return 0
                           
    def validar_contraseña(self, cont):
        punt=string.punctuation
        digits=string.digits
        abc=string.ascii_letters
        val_punt=0
        val_digits=0
        val_abc=0
        while True:
            self.validar_cadena_vacia(cont)
            try:
                if len(cont)<5 or len(cont)>12:
                    raise Exception
                for char in cont:
                    if char in punt:
                        val_punt=1
                    elif char in digits:
                        val_digits=1
                    elif char in abc:
                        val_abc=1
                    else:
                        raise Exception
                if val_abc==1 and val_digits==1 and val_punt==1:
                    break
            except:
                print("Contraseña no valida")



class LimteRetiroDiario(Exception):
    pass

