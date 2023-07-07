class CarritoCompra(): 
    __dniCliente : str 
    __idCarro : str 
    __precio_unitario : float 
    __cantidad : int 
    __item : str 

    def __init__(self,dniCliente,idCarro,precio_unitario,cantidad,item): 
        self.__dniCliente = dniCliente 
        self.__idCarro = idCarro 
        self.__precio_unitario = precio_unitario 
        self.__cantidad = cantidad 
        self.__item = item 

    def get_idcarro(self): 
        return self.__idCarro
    
    def get_dni(self): 
        return self.__dniCliente
    
    def get_precio(self): 
        return self.__precio_unitario
    
    def get_cantidad(self): 
        return self.__cantidad 
    
    def get_item(self): 
        return self.__item
    
    def get_total(self): 
        total = self.get_cantidad()*self.get_precio()
        return total 
    
    def __lt__(self,otro):
        return self.get_dni()<otro.get_dni()

    