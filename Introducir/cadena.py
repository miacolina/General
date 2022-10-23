import string
import sys


def solicitar_introducir_cadena(invite):

    while True:

        print(invite, end=": ")
        datoIntroducido = input()

        if len(datoIntroducido) > 0:
            return datoIntroducido


def solicitar_introducir_char(invite):

    while True:
        
        print(invite, end=": ")
        datoIntroducido = input()

        if len(datoIntroducido) == 0:
            
            print("Al menos debe indicar un carácter.", file=sys.stderr)
            
        elif len(datoIntroducido) > 1:
            
            print("Debe indicar un único carácter.", file=sys.stderr)
            
        else:
            
            return datoIntroducido


def solicitar_introducir_letra(invite):

    while True:
 
        datoIntroducido = solicitar_introducir_char(invite)

        if datoIntroducido in string.ascii_lowercase:
            
            return datoIntroducido
        
        elif datoIntroducido in string.ascii_uppercase:
            
            return datoIntroducido.lower()


def solicitar_introducir_palabra(invite):
   
    while True:

        datoIntroducido = solicitar_introducir_cadena(invite)

        for caracter in datoIntroducido:
            if caracter not in string.ascii_letters:
                break
        else:
            return datoIntroducido.lower()
