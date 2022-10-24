class nodoLista(object):
    
    info,sig = None,None

class Listadelistas(object):
    
    def __init__(self):
        self.inicio = None
        self.tam = 0
        
    def tam(lista):
        return lista.tam
    
    def criterio(dato, campo =None):
        dic = {}
        if (hasattr (dato, '__dict__')):
            dic = dato.__dict__
        if campo is None or campo not in dic:
            return dato
        else:
            return dic[campo]
    
    def insertar(lista,dato, campo = None):
        nodo = nodoLista()
        nodo.info = dato
        if (lista.inicio is None) or (criterio(lista.inicio.info, campo > criterio(dato,campo))):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while (act is not None and criterio(act.info, campo)< criterio(dato,campo)):
                ant = ant.sig
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        lista.tam += 1
        
    def buscar(lista, buscado, campo = None):
        aux = lista.inicio
        while (aux is not None and criterio(aux.info,campo) != criterio(buscado,campo):
            aux = aux.sig
        return aux

    def eliminar(lista, clave, campo = None):
        dato = None
        if(criterio(lista.inicio.info, campo) == criterio(clave,campo):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tam -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while (actual is not None and criterio(actual.info, campo) != criterio(clave,campo)):
                anterior = anterior.sig
                actual = actual.sig 
            if (actual is not None):
                dato = actual.info
                anterior.sig = actual.sig 
                lista.tam -= 1
        return dato
        
    def barrido(lista):
        aux = lista.inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig