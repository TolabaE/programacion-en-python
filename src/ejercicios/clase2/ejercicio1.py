# Escribir un programa en Python que pida al usuario que ingrese las medidas de la base y la altura de un rectángulo y muestre:

# 1.El perímetro del rectángulo
base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))

perimetro = (base * 2)  + (altura * 2)
print("el perimetro del rectangulo es",perimetro)

# 2.El área del rectángulo

area = base * altura
print("el area del rectangulo es",area)