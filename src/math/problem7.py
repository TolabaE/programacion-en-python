# CÁLCULO DE DISTANCIA ENTRE DOS PUNTOS
# ESCRIBIR UN PROGRAMA QUE CALCULE LA DISTANCIA ENTRE DOS PUNTOS EN UN PLANO CARTESIANO, DADOS SUS COORDENADAS. EL USUARIO DEBE INGRESAR LAS COORDENADAS DE AMBOS PUNTOS.
# ES UNA ESTRUCTURA DE CONTROL SECUENCIAL DE TIPO FUNCIONAL

def calculoDistancia(): 
    puntoA = input("ingrese las coordenada de los primeros punto separado por una coma ejemplo x,y: ").split(":",-1)
    puntoB = input("ingrese las coordenada de los segundos puntos separado por una coma ejemplo x,y: ").split(":",-1)
    
    X1 = int(puntoA[0].split(",")[0])
    Y1 = int(puntoA[0].split(",")[1])

    X2 = int(puntoB[0].split(",")[0])
    Y2 = int(puntoB[0].split(",")[1])

    distancia = ((X2-X1)**2 + (Y2-Y1)**2)**0.5
    print("la distancia desde el punto A y el punto B es igual a: "+str(distancia))