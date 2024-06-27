# Python un algoritmo que permita colocar las 2 notas de sus parciales y la de su TP y informarle si aprobó la cursada, si promociono la materia o no aprobó la cursada.

# a) Promoción: Aprobar los dos (2) exámenes parciales con una nota no inferior a 6 y obtener un promedio igual o superior a 7, y el TP Aprobado.
# b) Aprobar cursada: 2 parciales aprobados con nota 4 o más (promedio 4) y el TP aprobado.
# c) Desaprobada la cursada: no cumplir con b)


nota1 = int(input("Ingrese la nota del primer examen: "));
nota2 = int(input("Ingrese la nota del segundo examen: "));
tpFinal = int(input("""Ahora coloque el estado del trabajo practico,
                    1) Aprobado
                    2) Desaprobado
                    Elija un numero de acuerdo a su nota: """))

def calcularPromocion(examen1,examen2,proyecto):
    promedio = (examen1 + examen2) / 2;
    if(examen1 and examen2 >= 4 and proyecto == 1):
        if(promedio >= 7):
            print("El alumno a promocionado la materia")
        elif(promedio < 7):
            print("El alumno es regular de la materia y esta en condiciones de ir a final")
    else:
        print("El alumno a desaprobado y perdido la cursada de la materia")

calcularPromocion(nota1,nota2,tpFinal)