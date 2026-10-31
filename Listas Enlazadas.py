#Clase que representa la estructura de un nodo
class Nodo:
    def __init__(self, numero):
        #Valor que tendrá el nodo
        self.numero = numero

        #Apunta a nuestro siguiente nodo
        self.siguiente = None

#Clase que va a administrar todos los nodos
class ListasEnlazadas:
    def __init__(self):
        self.cabeza = None

    def Insertar_Nodo_Al_Inicio(self, numero):
        nuevo_nodo = Nodo(numero)

        if(self.cabeza is None):

            self.cabeza = Nodo(numero)

            return

        nuevo_nodo.siguiente = self.cabeza

        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self, numero):

        nuevo_nodo = Nodo(numero)

        if(self.cabeza == None):
            self.cabeza = nuevo_nodo
            return

        #Referencia temporal
        actual = self.cabeza

        while(actual.siguiente):
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def Borrar_Nodo_al_Final(self):
        actual = self.cabeza

        while(actual.siguiente.siguiente):
            actual = actual.siguiente

        actual.siguiente = None
          
    def Borrar_Nodo_al_Inicio(self):
        incio = self.cabeza
        self.cabeza = self.cabeza.siguiente
        inicio = None
    def Imprimir_ListaEnlazada(self):

        actual = self.cabeza

        while(actual):
            print(actual.numero, "->", end=" ")
            actual = actual.siguiente
        print("None")

Mi_lista = ListasEnlazadas()
Mi_lista.Insertar_Nodo_Al_Inicio(5)
Mi_lista.Insertar_Nodo_Al_Inicio(4)
Mi_lista.Insertar_Nodo_Al_Inicio(3)
Mi_lista.Insertar_Nodo_al_Final(7)
Mi_lista.Insertar_Nodo_al_Final(9)
Mi_lista.Imprimir_ListaEnlazada()
print("Ahora borramos al inicio y al final")
Mi_lista.Borrar_Nodo_al_Final()
Mi_lista.Borrar_Nodo_al_Inicio()
Mi_lista.Imprimir_ListaEnlazada()

