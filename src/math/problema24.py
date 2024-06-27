# Se requiere un algoritmo que calcule la factura de luz eléctrica. Para ello, se debe permitir el ingreso de Kw por mes.
# Para calcular el costo total se debe considerar que los primeros 30 Kw cuestan $6.03, los siguientes 90 cuestan $6.19, los siguientes 80 Kw $6.78 y los siguientes $7.24.

mensaje = "el consumo total de la luz es de: $"

consumoWatts = int(input("Ingrese la cantidad de kw consumidos durante el mes: "))

def calculoFacturaLuz(consumoLuz):
    total = 0
    if(consumoLuz >= 200 ):
        total = 30 * 6.03;
        total += 90 * 6.19
        total += 80 * 6.78
        total += (consumoLuz - 200) * 7.24 
        print(mensaje+str(total))
    elif(consumoLuz >= 120):
        total = 30 * 6.03
        total += 90 * 6.19
        total += (consumoLuz - 120) * 6.78
        print(mensaje+str(total))
    elif(consumoLuz < 120):
        total = 30 * 6.03;
        total += (consumoLuz - 30) * 6.19
        print(mensaje+str(total))
    elif(consumoLuz <= 30):
        total = consumoLuz * 6.03
        print(mensaje+str(total))

calculoFacturaLuz(consumoWatts)