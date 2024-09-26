# Crear una clase llamada Password con las siguientes condiciones:
import random

class Password:
    # atributo de clase privadas
    __LONGITUD = 8
    __CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    def __init__(self,longPassword) -> None:
        self.__contraseña = ""
        if(longPassword >= 6 and longPassword <= 15):
            self.__longitud = longPassword
        else:
            self.__longitud = self.__LONGITUD 

    # devuelve un booleano si es fuerte o no. Para que sea fuerte debe tener más de 1 mayúscula, 1 carácter especial, más de 1 minúscula y más de 1 números.
    def esFuerte(self):
        if(self.__contraseña == ""):
            print('No se genero ninguna contraseña, use el metodo generarPasword()')

        claveFuerte = False
        caracteres = "<=>@#%&+"
        mayuscula = 0
        minuscula = 0
        numero = 0
        caracter = 0

        for palabra in self.__contraseña:
            if(palabra.isupper()):
                mayuscula += 1
            if(palabra.islower()):
                minuscula +=1
            if(palabra.isdigit()):
                numero += 1
        
            for index in caracteres:
                if(palabra == index):
                    caracter +=1

        if(caracter != 0 and mayuscula > 1 and minuscula > 1 and numero > 1 ):
            claveFuerte = True
            return claveFuerte
        else:
            return claveFuerte
    
    # genera la contraseña del objeto cuyo valor de tipo string tendrá una longitud igual al valor del atributo de instancia “longitud”.
    # Para la generación de la clave puede usar los métodos random.choice() y string.join() de Python.
    def generarPassword(self):
        # en un ciclo for itero la cantidad de veces de acuerdo a la longuitud indicada.
        for i in range(self.__longitud):
            #en cada iteracion selecciona un caracter al azar y lo guarda en la variable.
            self.__contraseña += random.choice(self.__CARACTERES_VALIDOS)


    # Incluir métodos públicos que permitan obtener y asignar valores (getters y setters) a los atributos de instancia privados.
    # metodos publicos getter para obtener los valores del atributo privado contraseña
    @property
    def contraseña(self):
        return self.__contraseña

    # metodos publicos getter para obtener los valores del atributo privado longuitud
    @property
    def longuitud(self):
        return self.__longitud
    
    # metodos publicos setter para asignar valores a los atributos de instancia privados
    @contraseña.setter
    def contraseña(self,new_password):
        self.__contraseña = str(new_password)
        return self.__contraseña

    @longuitud.setter
    def longuitud(self,new_long):
        if(6 >= new_long <= 15):
            self.__longitud = new_long
        else:
            print("la longuitud de la contraseña no es la requerida,se asignara el valor por defecto")


    # Sobreescribir el método de instancia __str__(), para que retorne la clave generada y el valor booleano que devuelve el método “es_fuerte()”.
    def __str__(self) -> str:
        value = self.esFuerte()
        return f"la clave generada es: {self.__contraseña} y es fuerte: {value} "


# Luego, agregar sentencias de código Python que permitan:
# • Crear una lista de objetos de tipo Password.
# • Crear instancias de Password y agregarlas a la lista. Para cada objeto, se debe ingresar la
# longitud de la clave por teclado. Si el valor ingresado es cero, no se pasará ningún valor como argumento al método inicializador.
password1 = Password(11)
password2 = Password(4)
password3 = Password(15)
password4 = Password(0)
password5 = Password(8)
password6 = Password(6)


passwordList = [password1, password2, password3, password4, password5, password6]

# • Mostrar cada una de las contraseñas creadas y si es o no fuerte (usar un bucle). Para ello,
# usar este simple formato:
# contraseña1 - valor_booleano1
# contraseña2 - valor_bololeano2

for obj in passwordList:
    obj.generarPassword()
    value = obj.esFuerte()
    print(obj.contraseña,f"- {value}")


# login = Password(12)
# login.generarPassword()

# print(login.obtenerContraseña)
# login.longuitud = 20
# print(login.longuitud)

# print(login.contraseña)