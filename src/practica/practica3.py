# Escribir una función que reciba una muestra de números en una lista y retorne su media.

num_list = [6,6,10,15,30,100]

def calculoMedia(list):
    total = 0
    for num in list:
        total += num
    promedio = total // len(list)
    print("el promedio de los numeros ingresados es "+str(promedio))

calculoMedia(num_list)