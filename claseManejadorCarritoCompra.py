from claseCarritoCompra import CarritoCompra
import os 
import csv 
class ManejadorCarritoCompra(): 
    __lista = []

    def __init__(self): 
        self.__lista = []

    def carga(self): 
        archivo=open(os.getcwd()+'/archivos/carritoCompras.csv','r')
        reader=csv.reader(archivo,delimiter=';')

        archivo.__next__()
        for fila in reader: 
            carritocompra=CarritoCompra(fila[0],fila[1],float(fila[2]),int(fila[3]),fila[4])
            self.__lista.append(carritocompra)       
        archivo.close()

    def item_a(self,dni): 
        i = int(0)
        suma=0.0
        print("Carro     Cantidad     Precio Unitario   ItemPedido       Total")
        while i<(len(self.__lista)): 
            if(self.__lista[i].get_dni()==dni): 

                print("{:10} {:10} {:10} {:10} {}".format(self.__lista[i].get_idcarro(),self.__lista[i].get_cantidad(),self.__lista[i].get_precio(),self.__lista[i].get_item(),self.__lista[i].get_total()))
                suma=suma+self.__lista[i].get_total()
            i+=1
        print("TOTAL A PAGAR: {:20}".format(suma))

    def item_b(self,dni): 
        i = int(0)
        suma = float(0)

        while i<(len(self.__lista)): 
            if self.__lista[i].get_dni()==dni: 
                suma = suma+self.__lista[i].get_total()
            i+=1
        print("LA SUMA DE SUS COMPRAS ES :${}".format(suma))  

        if suma>70000: 
            descuento = suma - suma*0.10
        else: 
            descuento=0
        print("DESCUENTO A APLICAR EN LAS PROXIMAS COMPRAS: ${}".format(descuento))

    def item_c(self): 
        self.__lista.sort()

        for i in range (len(self.__lista)): 
            print(self.__lista[i].get_dni())

    


    