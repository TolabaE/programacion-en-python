# Crear una clase llamada Persona, Con los siguientes atributos privados:
# •nombre
# •edad
# •dni
# Y los siguientes métodos:
# •mostrar_edad(): retorna la edad de la persona
# •es_mayor_edad(): retorna True si edad es mayor o igual a 18, o False si es menor a 18.

# El método constructor __init__ de la clase debe recibir y asignar los valores a cada uno de los atributos privados de la clase.

class Persona:
    def __init__(self,nombre,edad,dni) :
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar_edad(self):
        return f"la edad de {self.nombre} es de {self.edad} años."
    
    def es_mayor_edad(self):
        if(self.edad >= 18):
            return f"{self.nombre} es mayor de edad."
        else:
            return f"{self.nombre} no es mayor de edad."


persona1 = Persona("eduardo",14,41357391)
persona2 = Persona("jorge",24,41327199)


print(persona1.mostrar_edad())
print(persona2.es_mayor_edad())