# 25. Se requiere un algoritmo que calcule el costo de internación de un paciente. Para ello, se debe solicitar que
# ingrese en que categoría se encuentra y la cantidad de días que se encuentra hospitalizado. Las categorías de internación son las siguientes:
# a. Pediatría
# b. Maternidad
# c. Otro
# Y los costros de internación por especialidad son los siguientes:
# d. Pediatría: $2.500
# e. Maternidad: $3.500
# f. Otro: $3.000

categoria = input("""Ingrese la categoria en la que se encuentra hospitalizado el paciente
                a.Pediatria
                b.Maternidad
                c.Otro
                Coloque la letra de acuerdo a la opción: """).lower()

dias = int(input("Ingrese la cantidad de dias que permanece hospitalizado: "))

mensaje = "El costo total por la internacion en el sector de "
mensaje_escape = "El valor ingresada no pertenece a ningun sector..."
segundo_texto = " es: $"

pediatria = "Pediatria"
maternidad = "Maternidad"
otros = "Otro"


def costoDeInternacion(sector,cantidad_dias):
    if(sector == "a"): 
        print(mensaje+pediatria+segundo_texto,cantidad_dias * 2500)
    elif(sector == "b"):
        print(mensaje+maternidad+segundo_texto,cantidad_dias * 3500)
    elif(sector == "c"):
        print(mensaje+otros+segundo_texto,cantidad_dias * 3000)
    else:
        print(mensaje_escape)

costoDeInternacion(categoria,dias)