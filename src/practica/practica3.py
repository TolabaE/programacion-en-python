# Escribir una función que reciba una muestra de números en una lista y retorne su media.

num_list = [4,4,6,10,15,20,40,80,10,99]

def calculoMedia(list):
    promedio = sum(num_list) / len(list)
    print("el promedio de los numeros ingresados es "+str(promedio))

calculoMedia(num_list)