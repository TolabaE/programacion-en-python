# ESCRIBIR UN PROGRAMA QUE CALCULE EL AREA DE UN CIRCULO, DADO SU RADIO. EL USUARIO DEBE INGRESAR EL VALOR DEL RADIO.
# ES UNA ESTRUCTURA DE CONTROL SECUENCIAL DE TIPO FUNCIONAL

def calcularRadio():
    radio = float(input("ingrese el radio(en cm) de un circulo para calcular su area: "))
    pi = 3.12
    areaCirculo = pi * (radio**2)
    print("el area del circulo es de: ",areaCirculo,"cm2")

calcularRadio()