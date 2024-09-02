# Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos y segundos.

def calculoSegundos(hs,minuto,seg):
    totalSeg = seg
    totalMinSeg = (minuto * 60)
    totalHsSeg = (hs * 3600)
    return [totalMinSeg,totalHsSeg,totalSeg]

sumaTotal = sum(calculoSegundos(3,30,50))


print("el valor de name en practica1 es ",__name__)

if __name__ == "__main__":
    print("el total de segundo es de: "+ str(sumaTotal)+" segundos")