#CALCULAR EDAD
# Escribir un programa que pida al usuario su año de nacimiento y muestre en pantalla su edad actual.
# ESTRUCTURA DE CONTROL SECUENCIAL.

import datetime

fechaActual = datetime.datetime.now().year

valor = input("ingrese el año de su nacimiento: ")

def calcularEdad(fechaNac): 
    edad = fechaActual - int(fechaNac);
    return edad

edad = calcularEdad(valor)
respuesta = "su edad actual es de: " + str(edad) + " años"
print(respuesta)