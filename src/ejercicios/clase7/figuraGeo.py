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


figura1 = Circulo(12)

figura1.perimetro()
figura1.area()