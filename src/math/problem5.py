# CALCULO DEL PROMEDIO DE NOTAS
# Escribir un programa que calcule el promedio de tres notas ingresadas por el usuario.
# ES UNA ESTRUCTURA DE CONTROL SECUENCIAL DE TIPO FUNCIONAL.

def calcularPromedio():
    primera_nota = input("Ingrese el valor de su primera nota: ")
    segunda_nota = input("Ingrese el valor de la segunda nota: ")
    tercera_nota = input("Ingrese el valor de la tercera nota: ")
    promedio = int(primera_nota)+int(segunda_nota)+int(tercera_nota)/3
    print("El promedio total de su nota es de: ",promedio)

calcularPromedio()