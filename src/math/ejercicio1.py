#SUMA DE DOS NUMEROS.
#Escribir un programa que pida al usuario dos números y muestren pantalla la suma de ambos.
#ESTO ES UNA ESTRUCTURA DE CONTROL SECUENCIAL CON FUNCIONES.

def sumarNumeros():
    primerValor = input("Ingrese el primer valor que desea sumar: ")
    segundoValor = input("Ingrese el segundo valor que va a sumar al primer: ")
    resultado = int(primerValor) + int(segundoValor)
    return print("el resultado de la suma es: "+ str(resultado))