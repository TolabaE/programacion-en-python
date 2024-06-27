# ESCRIBIR UN ALGORITMO QUE CALCULE LA RAÍZ CUADRADA DE UN NÚMERO INGRESADO POR EL USUARIO.
# ES UNA ESTRUCTURA DE CONTROL SECUENCIAL DE TIPO FUNCIONAL
import math

def calculoRaizCuadrada():
    numero = int(input("ingrese un numero que desea calcular su raiz cuadrada: "))
    raiz = math.sqrt(numero) #metodo que obtiene la raiz cuadrada.
    print("el resultado de la raiz cuadrada de",numero, "es igual a:",raiz)

calculoRaizCuadrada()