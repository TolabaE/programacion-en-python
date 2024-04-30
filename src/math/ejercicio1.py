#CALCULAR EDAD
# se asigna el valor a una variable de tipo entero, donde recibe como valor el año de nacimiento, luego calcula su edad.
# ESTRUCTURA DE CONTROL SECUENCIAL.

import datetime ;

fechaActual = datetime.datetime.now().year

valor = input("ingrese el año de su nacimiento: ")

def calcularEdad(fechaNac): 
    edad = fechaActual - int(fechaNac);
    return edad

edad = calcularEdad(valor)
respuesta = "su edad actual es de: " + str(edad) + " años"
print(respuesta)