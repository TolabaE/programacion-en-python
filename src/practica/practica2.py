# Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos,
# sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.

from practica1 import calculoSegundos

def calculoTotalSeg():
    # pido los dos intervalos de tiempos
    intervalo1 = input("Ingrese el primer intervalo de tiempo separados por una coma ejemplo => hs,minutos,seg: ").split(",")
    intervalo2 = input("Ingrese el segundo intervalo de tiempo: ").split(",") #usando el metodo split corto una cadena de texto por parametro y me los guarda en una lista.
    
    segTotal = 0
    segTotal = calculoSegundos(int(intervalo1[0]),int(intervalo1[1]),int(intervalo1[2])) + calculoSegundos(int(intervalo2[0]),int(intervalo2[1]),int(intervalo2[2])) 
    print("la suma total en segundos de los dos intervalos es "+ str(segTotal)+ " segundos")

calculoTotalSeg()