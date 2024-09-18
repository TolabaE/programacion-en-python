# Crear una clase llamada ListaDeTareas con los siguientes atributos y métodos:
# • Atributo de instancia privado “lista_tareas” de tipo list.
# • Método de instancia público “agregarTarea(tarea)”,
# que recibe como argumento una tarea que debe ser agregada a la lista de tareas (atributo “lista_tareas”) y retorna el string “Tarea agregada correctamente a la lista” ó “La tarea no fue agregada a la lista” en caso que la tarea se haya agregado o no a la lista respectivamente.
# • Método de instancia público “quitarTarea(tarea)”, que recibe como argumento una
# tarea que debe ser eliminada de la lista de tareas (atributo “lista_tareas”) y retorna el string “Tarea eliminada correctamente de la lista” ó “La tarea no fue eliminada de la lista” en caso que la tarea se haya eliminado o no de la lista respectivamente.
# • Método de instancia público “mostrarTareas()”, que no recibe ningún argumento y
# retorna la lista de tareas (atributo “lista_tareas”) .
# Luego, se debe crear una instancia de ListaDeTareas, agregar tareas a la lista, eliminar tareas de la lista y finalmente imprimir la lista completa de tareas.
# Nota: el método “quitarTarea(tarea)” debe validar si la tarea a eliminar existe en la lista antes de ser eliminada.

class ListaDeTareas:
    def __init__(self,) -> None:
        self.__list_tareas = []

    def agregarTarea(self,tarea):
        if(tarea in self.__list_tareas):
            return "la tarea ya existe en su lista"
        else:
            self.__list_tareas.append(tarea)
            return f"la tarea {tarea} fue agrega con exito a su lista."
    
    def quitarTarea(self,tarea):
        try:
            self.__list_tareas.remove(tarea)
            return f"La tarea '{tarea}' fue eliminada con éxito de su lista."
        except ValueError:
            return f"La tarea '{tarea}' no existe en su lista actualmente."


    def mostrarTareas(self):
        return self.__list_tareas

tareaEduardo = ListaDeTareas()

tareaEduardo.agregarTarea("lavar")
tareaEduardo.agregarTarea("cocinar")
print(tareaEduardo.agregarTarea("planchar"))
print(tareaEduardo.agregarTarea("planchar"))
print(tareaEduardo.quitarTarea("lavar"))
print(tareaEduardo.quitarTarea("limpiar"))
print(tareaEduardo.mostrarTareas())