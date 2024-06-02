# Se necesita de un algoritmo que calcule la cantidad de dinero que deberá pagar un cliente, teniendo en
# cuenta el monto total de la compra. Si el monto de la compra es superior a los $5.000 y el cliente paga en
# efectivo se le debe aplicar un descuento del 15%, si la compra es mayor a $5.000 y paga con tarjeta se le
# debe aplicar un descuento del 10%, si la compra es mayor a $2.000 se le debe aplicar un descuento del 10% y si es menor no posee descuento.


mensaje = [
        "Por realizar el pago con efectivo y aplicando el descuento del 15% por superar los $5000, el monto total a pagar es: $",
        "Por realizar el pago con tarjeta y aplicando el descuento del 10% por superar los $5000, el monto total a pagar es: $",
        "Por realizar el pago con tarjeta y aplicando el descuento del 10% por superar los $2000, el monto total a pagar es: $",
        "El monto total a pagar es de: $"
    ]

totalCompra = int(input("ingrese el valor total de la compra: "))
metodoPago = input("""Seleccione  el metodo de pago para realizar su compra:
                    1) pago en efectivo
                    2) pago con tarjeta
                    ingrese el valor: """)


def calcularPago(cantidad,pago):
    if(pago == "1"):
        if(cantidad>=5000):
            cantidad -= cantidad * 0.15
            print(mensaje[0],cantidad)
        else:
            print(mensaje[3],cantidad)
    else:
        if(cantidad>=5000):
            cantidad -= cantidad * 0.10
            print(mensaje[1],cantidad)
        elif(cantidad>=2000):
            cantidad -= cantidad * 0.10
            print(mensaje[2],cantidad)
        else:
            print(mensaje[3],cantidad)


calcularPago(totalCompra,metodoPago)