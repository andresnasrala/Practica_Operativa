from claseManejadorCarritoCompra import ManejadorCarritoCompra
from claseManejadorCliente import ManejadorCliente 

class Menu(): 
    __switch : int 

    def __init__(self): 
        self.__switch : None 

    def cartelera(self): 
        print("Item a=1")
        print("Item b=2")
        print("Item c=3")
        print("salir = 0")

    def Ejecutar(self): 
        manager_cliente=ManejadorCliente()
        manager_compra=ManejadorCarritoCompra()
        manager_cliente.carga()
        manager_compra.carga()
        self.cartelera()
        self.__switch = int(input("Ingrese un numero comenzar a operar: "))

        while self.__switch != 0 and self.__switch<=3: 

            if self.__switch == 1: 
                dni = input("Ingrese el dni a buscar: ")
                manager_cliente.item_a(dni,manager_compra)
            elif self.__switch == 2: 

                alias=input("Ingrese el alias para buscar: ")
                manager_cliente.item_b(alias,manager_compra)
                
            elif self.__switch ==3: 
                manager_compra.item_c()

            self.__switch = int(input("Ingrese un numero comenzar a operar: "))

