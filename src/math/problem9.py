# ESCRIBIR UN PROGRAMA QUE CALCULE EL AREA DE UN CIRCULO, DADO SU RADIO. EL USUARIO DEBE INGRESAR EL VALOR DEL RADIO.
# ES UNA ESTRUCTURA DE CONTROL SECUENCIAL DE TIPO FUNCIONAL
import math


def calcularRadio():
    radio = input("ingrese el radio(en cm) de un circulo para calcular su area: ")
    pi= 3.14
    areaCirculo = pi * (int(radio,base=0)**2)
    print("el area del circulo es de: ",areaCirculo,"cm")