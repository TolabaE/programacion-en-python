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
        if(self.__contraseña == ''):
            print('No se genero ninguna contraseña, use el metodo generarPasword()')

        mayuscula = 0
        minuscula = 0
        numero = 0
        caracteres = "<=>@#%&+"
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

        if(caracter != 0 and mayuscula != 0 and minuscula != 0 and numero != 0 ):
            return True
        
        print('la contraseña generada es :',self.__contraseña)


    
    # genera la contraseña del objeto cuyo valor de tipo string tendrá una longitud igual al valor del atributo de instancia “longitud”.
    # Para la generación de la clave puede usar los métodos random.choice() y string.join() de Python.
    def generarPassword(self):
        # en un ciclo for itero la cantidad de veces de acuerdo a la longuitud indicada.
        for i in range(self.__longitud):
            #en cada iteracion selecciona un caracter al azar y lo guarda en la variable.
            self.__contraseña += random.choice(self.__CARACTERES_VALIDOS)


    # Incluir métodos públicos que permitan obtener y asignar valores (getters y setters) a los atributos de instancia privados.

    # Sobreescribir el método de instancia __str__(), para que retorne la clave generada y el valor booleano que devuelve el método “es_fuerte()”.<










login = Password(12)

login.generarPassword()
login.esFuerte()