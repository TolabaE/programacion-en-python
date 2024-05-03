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