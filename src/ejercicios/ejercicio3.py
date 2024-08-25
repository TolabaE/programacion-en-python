# Escribe un programa en Python que solicite al usuario 5 números enteros. Luego imprimir el máximo y el mínimo de los valores ingresados. El programa deberá permitir el ingreso de valores iguales.

num_list = [];

for(i) in range(5):
    num = int(input("Ingrese el "+str(i+1) +" numero: "))
    num_list.append(num) #metodo para agregar un valor en una lista,siempre en la ultima posicion.
    num_list.sort() #metodo que ordena la lista

print("el menor valor ingresado es: ", num_list[0]) 
print("el mayor valor ingresado es: ", num_list[-1])
