# CALCULAR EL AREA DE UN TRIANGULO.
# Escribir un programa que calcule el área de un triángulo, dados su base y altura. El usuario debe ingresar la base y la altura.
# ES UNA ESTRUCTURA DE CONTROL SECUENCIAL DE TIPO FUNCIONAL

def areaTriangulo():
    base = input("ingrese la base del triangulo en cm: ")
    altura = input("Ahora ingrese la altura del triangulo en cm: ")
    areaTriangulo = (int(base)*int(altura))/2
    print("la area total del triangulo es de: ",areaTriangulo,"cm")