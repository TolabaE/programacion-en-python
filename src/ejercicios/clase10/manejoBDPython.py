import sqlite3


class ManejoBaseDatos:
    def __init__(self,nombre_bd:str):
        self.name_conexion = nombre_bd
        self.__cursor:float

    def realizarConexionBD(self):
        self.__bd_conection = sqlite3.connect(f"./src/ejercicios/clase10/{self.name_conexion}.db")
        self.__cursor = self.__bd_conection.cursor()
        # creamos la conexion  con la base
        print("conexion realizada con exito")

    def crearTabla(self):
        self.realizarConexionBD()
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nro_legajo INTEGER UNIQUE NOT NULL UNIQUE,
                dni INTEGER NOT NULL,
                nombre TEXT NOT NULL,   
                apellido TEXT NOT NULL,
                area TEXT NOT NULL
            )
        """)

        # confirmo los cambios
        self.__bd_conection.commit()

    def insertarRegistro(self,nuevo_registro):
        self.__cursor.execute(f"INSERT INTO {self.name_conexion} (nro_legajo, dni, nombre, apellido, area) VALUES (?, ?, ?, ?, ?)", nuevo_registro)
        self.__bd_conection.commit()
        print("usuario ingresado con exito")
    
    def seleccionarRegistro(self,dni:int):
        # self.realizarConexionBD()
        self.__cursor.execute(f"SELECT * FROM {self.name_conexion} WHERE dni=?",(dni,))
        usuario = self.__cursor.fetchone()
        if (usuario):
            print(usuario)  
        else:
            print(f"Error,No existe un usuario con el dni {dni} ingresado.")
        
    # Selecionar todos los empleados o los registros de la tabla.
    def seleccionarTodosRegistros(self):
        # self.realizarConexionBD()
        self.__cursor.execute(f"SELECT * FROM {self.name_conexion}")
        usuarios = self.__cursor.fetchall()
        if (usuarios):
            for user in usuarios:
                print(user)  
        else:
            print(f"Error, la tabla que desea consultar esta vacia")

    # Modificar el area de un empleado en función de su numero de legajo.
    def modificarEmpleado(self,legajo:int,nuevo_dato:str):
        existe = self.__cursor.execute(f"SELECT * FROM {self.name_conexion} WHERE nro_legajo=?",(legajo,)).fetchone()
        # print(existe == None)
        if (not existe):
            print(f"el usuario con el lejago numero {legajo} no existe en la tabla")
        else:
            self.__cursor.execute(f"UPDATE {self.name_conexion} SET area=? WHERE nro_legajo=?",(nuevo_dato,legajo))
            self.__bd_conection.commit()
            print("se actualizo el dato en la base de datos con exito!")

    # Eliminar un empleado a partir del numero de legajo.
    def eliminarEmpleados(self,legajo):
        self.realizarConexionBD()
        self.__cursor.execute(f"DELETE FROM {self.name_conexion} WHERE nro_legajo=?",(legajo,))
        self.__bd_conection.commit()

def main(nombre_base):
    empleados = ManejoBaseDatos(nombre_base)
    empleados.realizarConexionBD()
    valor = int(input("""ingrese el numero de acuerdo a las accion que desea realizar:
                Opcion 1 Insertar un registro de empleado.
                Opcion 2 Selecionar un registro de empleado a partir de su numero DNI.
                Opcion 3 Selecionar todos los empleados o los registros de la tabla.
                Opcion 4 Modificar el area de un empleado en función de su numero de legajo.
                Opcion 5 Eliminar un empleado a partir del numero de legajo.
                ingrese: """))

    if(valor == 1):
        nuevo_registro = input("ingrese el nuevo empleado separado por una coma y respetando el orden (legajo / dni/ nombre / apellido / area): ").split(",")
        empleados.insertarRegistro(nuevo_registro)


main("empleados")














# empleados.crearTabla()
# empleados.insertarRegistro(120240,2212991,"Florencia","Perichon","auxiliar digital")
# empleados.insertarRegistro(191892,4225166,"leandro","amaya","armador digital")
# empleados.seleccionarRegistro(4212991)    

# empleados.seleccionarTodosRegistros()
# empleados.modificarEmpleado(192779,"almagro")
# empleados.eliminarEmpleados(192448)
