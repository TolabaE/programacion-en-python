# 27. Se requiere un algoritmo que solicite ingresar:
# a. Nombre del Artículo.
# b. Precio o costo unitario.
# c. Número de departamento en donde se localiza el producto.
# En base a los datos ingresados se deberá calcular el incremento de los costos del producto y mostrar el costo final.

# departamento 1 => 10% incremento
# departamento 2 => 15% incremento
# departamento 3 => 20% incremento
# departamento otros => 5% incremento


articulo = input("ingrese el nombre del articulo: ")
costoUnitario = int(input("Ingrese el precio unitario del producto: "))
departamento = int(input("Ingrese el sector donde se encuentra el producto, ¡recuerde que existe 4 categorias! : "))

mensaje = "el costo final del producto "
mensajeError = "lo sentimos el numero ingresado no pertenece a ningun sector :("

def calcularCostoProducto(producto,precio,sector):
    if(sector == 1):
        precio += precio * 0.10
        print(mensaje+producto+" es de: $"+str(precio))
    elif(sector == 2):
        precio += precio * 0.15
        print(mensaje+producto+" es de: $"+str(precio))
    elif(sector == 3):
        precio += precio * 0.20
        print(mensaje+producto+" es de: $"+str(precio))
    elif(sector == 4):
        precio += precio * 0.5
        print(mensaje+producto+" es de: $"+str(precio))
    else:
        print(mensajeError)

calcularCostoProducto(articulo,costoUnitario,departamento)