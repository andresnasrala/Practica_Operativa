class Cliente(): 
    __dniCliente : str 
    __apellido : str 
    __nombre : str 
    __alias : str 

    def __init__(self,dniCliente,apellido,nombre,alias): 
        self.__dniCliente = dniCliente 
        self.__apellido = apellido 
        self.__nombre = nombre 
        self.__alias = alias 

    def get_dni(self): 
        return self.__dniCliente
    
    def get_ayn(self): 
        return self.__apellido+' '+self.__nombre
    
    def get_alias(self): 
        return self.__alias 