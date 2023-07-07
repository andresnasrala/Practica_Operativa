import os 
import csv 
from claseCliente import Cliente 

class ManejadorCliente(): 
    __lista = []

    def __init__(self): 
        self.__lista = []

    def carga(self):
        archivo=open(os.getcwd()+'/archivos/clientes.csv','r')
        reader=csv.reader(archivo,delimiter=';')

        archivo.__next__()
        for fila in reader: 
            cliente=Cliente(fila[0],fila[1],fila[2],fila[3])
            self.__lista.append(cliente)       
        archivo.close()

    def item_a(self,dni,manager_compra): 
        i = int(0)
        bandera=False
        while i<(len(self.__lista)) and bandera==False: 
            if self.__lista[i].get_dni()==dni: 
                bandera = True 
            i+=1
        if not bandera: 
            print('cliente no encontrado')
        else: 
            print("DNI: {}        APELLIDO Y NOMBRE: {} ".format(self.__lista[i].get_dni(),self.__lista[i].get_ayn()))
            manager_compra.item_a(dni)
    
    def item_b(self,alias,manager_compra): 
        i = int(0)
        bandera = False 
        
        while i<(len(self.__lista)) and not bandera: 
            if(self.__lista[i].get_alias()==alias): 
                bandera=True 
            i+=1

        if not bandera: 
            print('cliente no encontrado')
        else: 
            manager_compra.item_b(self.__lista[i].get_dni())
            


    

