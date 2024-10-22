import math


class FiguraGeometrica:
    colo_fondo: str
    color_borde:str
    
    def __init__(self):
        pass
    
    def area():float
    
    def perimetro():float


class Circulo(FiguraGeometrica):
    def __init__(self,radio:int):
        super().__init__()
        self.radio = radio

    def perimetro(self):
        perimetro = 2 * math.pi * self.radio
        print(f"el perimetro del circulo es {perimetro:.2f}")

    def area(self):
        area = math.pi * self.radio ** 2
        print(f"el area del circulo es {area:.2f}")


class Triangulo(FiguraGeometrica):
    def __init__(self,base:int,altura:int):
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self):
        area = (self.base * self.altura) / 2
        print(f"la area del triangulo es de {area:.2f}")
    
    def perimetro(self):
        ladoA = int(input("ingrese la medida del lado a del triangulo: "))
        ladoB = int(input("ingrese la medida del lado b del triangulo: "))
        perimetro = ladoA + ladoB + self.base
        print(f"el perimetro del triangulo es de {perimetro:.2f}")


class Rectangulo(FiguraGeometrica):
    def __init__(self,base:int,altura:int):
        super().__init__()
        self.base = base
        self.altura = altura

    def perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        print(f"el perimetro del rectangulo es {perimetro:.2f}")

    def area(self):
        area = self.base * self.altura
        print(f"la area del rectangulo es {area:.2f}")


# pruebas con el rectangulo
figuraRectangular = Rectangulo(8,12)
figuraRectangular.area()
figuraRectangular.perimetro()


# pruebas con el triangulo
figuraTriangular = Triangulo(6,4)
figuraTriangular.perimetro()
figuraTriangular.area()


# pruebas con el circulo
figura1 = Circulo(12)
figura1.perimetro()
figura1.area()