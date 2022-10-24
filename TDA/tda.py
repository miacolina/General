import sys
from .tda_pila import (
    Pila, 
    apilar,  
    desapilar, 
    pila_vacia,
)
from .tda_cola import (
    Cola, 
    arriba, 
    atencion, 
    cola_vacia,
)
from .tda_lista import(
    Lista, 
    insertar,
    buscar, 
    eliminar, 
    barrido,
)
from .tda_lista_lista import (
    Listadelistas,
    insertar,
    buscar,
    barrido
)
def pila():
    pdatos = Pila()
    ppar = Pila()
    pimpar = Pila()
    dato = int(input('Ingrese un número -0 para salir'))

    while (dato != 0):
        apilar(pdatos,dato)
        dato = int(input('Ingrese un número -0 para salir'))

    while (not pila_vacia(pdatos)):
        dato= desapilar(pdatos)
        if (dato % 2 == 0):
            apilar(ppar,dato)
        else:
            apilar (pimpar,dato)
        
    while (not pila_vacia(ppar)):
        dato = desapilar(ppar)
        print(dato)
    
    while (not pila_vacia(pimpar)):
        dato = desapilar(pimpar)
        print(dato)
    
def cola():
    cdatos = Cola()
    cvocales = Cola()
    letra = input('Ingrese un caracter')
    while (letra != ''):
        arriba(cdatos,letra)
        letra = input('Ingrese un caracter')

def listas():
    lista = Lista()
    dato = input('Ingrese una palabra')
    
    while(dato != ''):
        insertar(lista,dato)
        datos = input('Ingrese una palabra')
        
    buscado = input('Ingrese la palabra a buscar')
    posicion = buscar(lista, buscado)
    
    if (posicion is not None):
        dato = eliminar(lista, posicion.info)
        print('Elemento eliminado', dato)
    else:
        print('No se encontro el elemento a eliminar')
    barrido(lista)

def listadelistas():
    estaciones =Lista()
    dato = input('Ingrese nombre de la estación:')
    