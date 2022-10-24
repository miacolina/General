from pickle import OBJ
import sys

class nodoCola (object):
    info, sig = None, None
    
class Cola(object):
    
    def __init__(self):
        self.frente, self.final = None, None
        self.tam = 0
        
    def arriba(cola, dato):
        nodo = nodoCola
        nodo.info =dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.tam += 1
    
    def atencion(cola):
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
        cola.tam -= 1
        return dato
    
    def cola_vacia(cola):
        return cola.frente is None
    
    def en_frente(cola):
        return cola.frente.info        
    
    def tam(cola):
        return cola.tam
    
    def mover_al_final(cola):
        dato = atencion(cola)
        arriba(cola, dato)
        return dato
    
    def barrido(cola):
        i = 0
        while (i < tam(cola)):
            dato = mover_al_final(cola)
            print(dato)
            i += 1
            
        