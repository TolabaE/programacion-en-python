from datetime import date
from datetime import datetime
from abc import abstractmethod,ABC



class CuentaBancaria:
    
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




cliente1 = CuentaBancaria(12345,182983,"edu.mp",15000,[])
cliente1.depositar(1200)

print(cliente1.movimientos)