#20. Se necesita un algoritmo que permita al usuario el ingreso de dos números e informe al usuario si el primer
#número ingresado es mayor al segundo, si la situación es al revés o si son iguales.

num1 = input("ingrese el primer numero  ")
num2 = input("ingrese el segundo numero  ")

num1mayornum2 = "el numero "+ num1 + " es mayor al numero "+num2
num2esMayoranum1 = "el numero "+num2+" es mayor al numero "+ num1
numerosIguales = "Ambos numeros son iguales"


def calcularMayor(numero1,numero2):
    if(numero1 > numero2) :
        print(num1mayornum2)
    elif(numero1<numero2):
        print(num1mayornum2)
    else:
        print(numerosIguales)

calcularMayor(num1,num2)
