# Se requiere un algoritmo que solicite ingresar:
# a. Importe de ventas de refacciones.
# b. Importe de ventas de servicio.
# c. Importe de ventas de autos y camiones.

# Calcule el importe TOTAL sumando los tres importes anteriores y el promedio de ventas (TOTAL / 3) y muestre al usuario los resultados de este cálculo. Si el promedio de ventas es mayor o igual a $50.000
# deberá mostrar el mensaje: “Se alcanzó el objetivo” de lo contrario deberá mostrar el mensaje “Buscar nuevas estrategias de ventas”.


venta_refaccion = int(input("Ingrese el importe total en ventas de refacciones: $"))
venta_servicio = int(input("Ingrese el importe total en ventas de servicios: $"))
venta_vehiculos = int(input("Ingrese el importe total en ventas de vehiculos: $"))

mensaje_alcanzado = "Se alcanzó el objetivo"
mensaje_faltante = "Buscar nuevas estrategias de ventas"
mensaje_promedio = "El promedio total de las 3 ventas es: $"

def calculoPromedioVentas(refaccion,servicio,vehiculos):
    promedioTotal = (refaccion+servicio+vehiculos) // 3
    print(mensaje_promedio+str(promedioTotal))
    if(promedioTotal>=50000):
        print(mensaje_alcanzado)
    else:
        print(mensaje_faltante)


calculoPromedioVentas(venta_refaccion,venta_servicio,venta_vehiculos)