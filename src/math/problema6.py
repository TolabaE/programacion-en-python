# CONVERSION DE MONEDA
# Escribir un programa que convierta una cantidad de pesos argentinos a dólares estadounidenses, utilizando un tipo de cambio fijo. El usuario debe ingresar la cantidad de pesos.

def convertirMoneda():
    valor = input("ingrese el valor de la moneda en pesos ARG que quiere pasar a dolar: ")
    dolarUSD = int(valor) / 877
    print("su cambio de ",valor, "pasado  a dolar le da como resultado: usd ",dolarUSD)

convertirMoneda()