# CALCULO DEL PROMEDIO DE NOTAS
# Escribir un programa que calcule el promedio de tres notas ingresadas por el usuario.
# ES UNA ESTRUCTURA DE CONTROL SECUENCIAL DE TIPO FUNCIONAL.

def calcularPromedio():
    primera_nota = float(input("Ingrese el valor de su primera nota: "))
    segunda_nota = float(input("Ingrese el valor de la segunda nota: "))
    tercera_nota = float(input("Ingrese el valor de la tercera nota: "))
    promedio = primera_nota + segunda_nota + tercera_nota/3
    print("El promedio total de su nota es de: ",promedio)

calcularPromedio()