# Se requiere de un algoritmo que permita al usuario ingresar 3 números distintos e indique cuál de ellos es el mayor.

num2 = int(input("Ingrese el valor del segundo numero: "))
num1 = int(input("Ingrese el valor del primer numero: "))
num3 = int(input("Ingrese el valor del tercer numero: "))


number_list = [num1,num2,num3]
number_list.sort()

messages = "El numero con mayor valor es el:"

print(messages,number_list[-1])