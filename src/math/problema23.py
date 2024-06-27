# Se requiere un algoritmo que calcule el sueldo neto de un trabajador. Para ello, el algoritmo debe admitir el ingreso del monto a cobrar por horas y el total de horas trabajadas. Si el empleado trabajo más de 160 horas
# mensuales se deben considerar la diferencia como horas extras y el monto por hora deberá ser el doble del valor ingresado en un inicio.

sueldo = int(input("Ingrese el sueldo del trabajador: "))
horas = int(input("Ingrese la cantidad de horas trabajadas del empleado: "))

mensaje = "el monto total por las horas trabajadas es de: $"

def calculoSueldo(salario,cantidad_Horas):
    if(cantidad_Horas > 160):
        sueldoExtra = (cantidad_Horas - 160) * (salario * 2)
        sueldoLaboral = 160 * salario
        sueldoTotal = sueldoLaboral + sueldoExtra
        print(mensaje+str(sueldoTotal))
    else:
        sueldoTotal = salario * cantidad_Horas
        print(mensaje+str(sueldoTotal))

calculoSueldo(sueldo,horas)