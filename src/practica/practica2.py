# Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos,
# sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.

import practica1 as p

def calculoTotalSeg():
    # pido los dos intervalos de tiempos
    intervalo1 = input("Ingrese el primer intervalo de tiempo separados por una coma ejemplo => hs,minutos,seg: ").split(",")
    intervalo2 = input("Ingrese el segundo intervalo de tiempo: ").split(",") #usando el metodo split corto una cadena de texto por parametro y me los guarda en una lista.

    segInt1 = p.calculoSegundos(int(intervalo1[0]),int(intervalo1[1]),int(intervalo1[2]))
    segInt2 = p.calculoSegundos(int(intervalo2[0]),int(intervalo2[1]),int(intervalo2[2]))

    hs = int(segInt1[0]) + int(segInt2[0])
    minutos = int(segInt1[1]) + int(segInt2[1])
    segundos = int(segInt1[2]) + int(segInt2[2])

    #si la suma de sus segundos es mayor a 60 entonces
    if(segundos >= 60):
        minutos = minutos + 60 # a los minutos le sume 60 segundos y el resto de seg que sea el nuevo resto.
        segundos = segundos - 60 
    
    #si a la suma de los minutos en segundos en mayor a 3600 
    if(minutos >= 3600):
        hs = hs + 3600 #entonces se agrega 3600 seg a la hora.
        minutos = minutos - 3600

    horas = hs // 3600
    minutos = minutos // 60
    print("la suma total en segundos de los dos intervalos es "+ str(horas)+ "hs "+str(minutos)+"min "+str(segundos)+"segundos")

print("el valor de name en practica2 es ",__name__)

if __name__ == "__main__":
    calculoTotalSeg()