# Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos y segundos.

def calculoSegundos(hs,minuto,seg):
    totalSeg = 0
    totalSeg += seg
    totalSeg += (minuto * 60)
    totalSeg += (hs * 3600)
    return totalSeg


# print("el total de segundo es de: "+ str(calculoSegundos(1,20,20))+" segundos")