

numeros = [1,5,-2]

def agregar_una_vez(lista:list, elemento):
    if elemento in lista:
        raise ValueError(f"Error: Imposible añadir elementos duplicados => {elemento}")
    else:
        lista.append(elemento)
        print(lista)


def main(elementos,valores):
    agregar_una_vez(elementos,valores)


main(numeros,"hola")
