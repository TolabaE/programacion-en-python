import random

# Ejemplo con una lista
frutas = ['manzana', 'banana', 'cereza', 'mango']
fruta_aleatoria = random.choice(frutas)
print(fruta_aleatoria)

# Ejemplo con una cadena
letra_aleatoria = random.choice('Python')
print(letra_aleatoria)


# Unir una lista de palabras con un espacio
palabras = ['Hola', 'mundo', 'Python', 'es', 'genial']
frase = ' '.join(palabras)
print(frase)  # Output: "Hola mundo Python es genial"

# Unir con un guion
palabras_con_guion = '-'.join(palabras)
print(palabras_con_guion)  # Output: "Hola-mundo-Python-es-genial"