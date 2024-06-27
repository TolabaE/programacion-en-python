# CÁLCULO DE DISTANCIA ENTRE DOS PUNTOS
# ESCRIBIR UN PROGRAMA QUE CALCULE LA DISTANCIA ENTRE DOS PUNTOS EN UN PLANO CARTESIANO, DADOS SUS COORDENADAS. EL USUARIO DEBE INGRESAR LAS COORDENADAS DE AMBOS PUNTOS.
# ES UNA ESTRUCTURA DE CONTROL SECUENCIAL DE TIPO FUNCIONAL
import math


def calculoDistancia(): 
    puntoA = input("ingrese las coordenada de los primeros punto separado por una coma ejemplo x,y: ").split(":",-1)
    puntoB = input("ingrese las coordenada de los segundos puntos separado por una coma ejemplo x,y: ").split(":",-1)
    
    X1 = float(puntoA[0].split(",")[0])
    Y1 = float(puntoA[0].split(",")[1])

    X2 = float(puntoB[0].split(",")[0])
    Y2 = float(puntoB[0].split(",")[1])

    distancia = math.sqrt(pow(X2-X1,2) + pow(Y2-Y1,2)) #la funcion pow() nos permite elevar la potenica de cualquier numero, y el metodo sqrt()calcula la raiz cuadrada.
    print("la distancia desde el punto A y el punto B es igual a: ",distancia)

calculoDistancia()