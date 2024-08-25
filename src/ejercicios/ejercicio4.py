# Escribe un programa en Python que solicite 5 números enteros al usuario. El mismo debe indicar si entre dichos valores hay números duplicados o no, imprimiendo por pantalla “HAY DUPLICADOS” o “SON TODOS DISTINTOS”.

list_num = []

for(i) in range(5):
    num = int(input("ingrese el "+str(i+1)+"° numero: "))
    list_num.append(num)


if(len(list_num) == len(set(list_num))): #el metodo set() se utiliza para crear elementos unicos elimina duplicados.
    print("no hay valores duplicados")
else:
    print("hay valores duplicados")