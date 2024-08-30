#AQUI TENEMOS LOS TIPOS DE DATOS QUE SE PUEDEN ESCRIBIR EN PYTHON DE FORMATO STRING

cadena_larga = """Hola este es un texto que puede
abarcar multiples lineas sin necesidad de 
estar desclarando texto abajo de otro"""


saludo = "Hola mundo este es mi primer paso en python"

numeroString = "2024";

#para recortar palabras de una cadena de texto
primera_palabra = saludo[0:4]


print(len(saludo))#calcula la longuitud de caracter.

#OPERADOR DE CONCATENACION
nombre = "camila"
apellido ="cardozo"

nombre_completo = nombre + apellido

#SEGUNDA FORMA DE CONCATENAR

#la f es un operador de formateo.
nombreCompleto = f"{nombre} {apellido}"


#METODOS CON STRINGS

texto = "asi es la vida al final que nos queda, tu esocojiste el camino y yo la vereda"

print(texto.upper())#pasa todo a mayuscula
print(texto.lower())#pasa todo a minuscula
print(texto.capitalize())#convierte la primera letra en mayuscula
print(texto.title())#convierte todas las primeras palabras en mayuscula
print(texto.strip())#elimina todos los espacios de la izquierda a la derecha
print(texto.find("camino"))#busca ela palabras que le pasen por parametro, y retorna la posicion
print(texto.replace("vida","comida"))#reemplaza el texto que le pasemos por otro.
print("la" in texto)#retorna true o false si se encuentra la palabra que estamos buscando.
print("caballo" not in texto)#lo mismo pero a la inversa.

# SECUENCIAS DE ESCAPE

comillas_doble = 'escribir en la consola "Hola mundo" para imprimir por pantalla'

otra_forma = "escribir en la consola \"HOLA DEV\" para imprimir en pantalla"

    # paso los intervalos que estan en un lista a numeros
    lista_num = []
    for num in intervalo1:
        lista_num.append(int(num))
    for num in intervalo2:
        lista_num.append(int(num))