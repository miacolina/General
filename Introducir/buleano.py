
SI = ("o", "sí", "y", "yes", "1")
VERDADERO = ("v", "verdadero", "t", "true", "1")

def solicitar_introducir_si_o_no(invite):
    try:
        return input(invite).lower() in SI
    except:
        return False

def solicitar_introducir_verdadero_o_falso(invite):
    try:
        return input(invite).lower() in VERDADERO
    except:
        return False