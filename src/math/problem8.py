# ESCRIBIR UN ALGORITMO QUE CALCULE LA RAÍZ CUADRADA DE UN NÚMERO INGRESADO POR EL USUARIO.
# ES UNA ESTRUCTURA DE CONTROL SECUENCIAL DE TIPO FUNCIONAL

def calculoRaizCuadrada():
    numero = int(input("ingrese un numero que desea calcular su raiz cuadrada: "))
    # print(type(numero))
    raiz = int((numero)**0.5)
    print("el resultado de la raiz cuadrada de",numero, "es igual a:",raiz)
    