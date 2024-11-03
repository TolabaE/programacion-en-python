from datetime import date
from datetime import datetime
from abc import abstractmethod,ABC


# clase abstracta
class CuentaBancaria(ABC):
    
    def __init__(self,nro_cuentas:str,cbu:str,alias:str,saldo:float,movimientos:list):
        self.nro_cuenta = nro_cuentas
        self.cbu = cbu
        self.alias = alias
        self.saldo = saldo
        self.movimientos = movimientos 

    #retorna del saldo en la cuenta
    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self,monto_a_depositar:float):
        self.saldo += monto_a_depositar
        hora_actual = datetime.now().time().replace(microsecond=0)#obtengo la hora actual
        fecha_actual = date.today() #año/mes/dia
        historial = (f"{fecha_actual}",f"{hora_actual}","deposito",monto_a_depositar,f"saldo: ${self.saldo}")
        self.movimientos.append(historial)
        return True
    
    # metodos abstractos
    @abstractmethod
    def extraer(self):
        pass

    # metodos abstractos
    @abstractmethod
    def transferir(self):
        pass


class CajaDeAhorro(CuentaBancaria):

    def __init__(self, nro_cuentas, cbu, alias, saldo, movimientos, monto_limite_extracciones:float,monto_limite_transferencia:float,cant_extracciones_disponible:int,cant_transferencia_disponible:int):
        super().__init__(nro_cuentas, cbu, alias, saldo, movimientos)
        self.limite_extraccion = monto_limite_extracciones
        self.limite_transferencia = monto_limite_transferencia
        self.cant_extracciones_disponible = cant_extracciones_disponible
        self.cant_transferencia_disponible = cant_transferencia_disponible

    def extraer(self,monto_a_extraer:float):
        saldo = self.consultar_saldo() # invoco al metodo para verificar su saldo en cuenta
        if(monto_a_extraer == 0): return f"no se puede realizar una trasferencia de 0 , intente otro monto"
        if(monto_a_extraer > saldo): return f"el limite de dinero a extraer  es superior a la cantidad disponible"

        if(monto_a_extraer <= self.limite_extraccion and self.cant_extracciones_disponible > 0):
            self.saldo = self.saldo - monto_a_extraer
            self.cant_extracciones_disponible -= 1 
            print("su extracion a sido realizo correctamente")
        else:
            print("el limite de dinero a extraer superior a la cantidad disponible")



usuario1 = CajaDeAhorro("12345", "11030", "eduardo-cbu19", 112000, [], 50000, 100000, 5, 10)

# cliente1 = CuentaBancaria(12345,182983,"edu.mp",15000,[])
# cliente1.depositar(1200)

response = usuario1.extraer(0)
print(response)
# print(cliente1.movimientos)