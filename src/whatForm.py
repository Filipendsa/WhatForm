import math
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def exibir(self):
        pass

class Quadrilatero(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
class Triangulo(Quadrilatero):
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.base + 2 * math.sqrt(self.base**2 + self.altura**2)
    
    def exibir(self):
        return "\n".join(["*" * (i + 1) for i in range(self.altura)])
    
class Quadrado(Quadrilatero):
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 4 * self.base
    
    def exibir(self):
        return "\n".join(["*" * self.base] * self.altura)
    
class Retangulo(Quadrilatero):
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def exibir(self):
        return "\n".join(["*" * self.base] * self.altura)
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio**2
    
    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def exibir(self):
        return "Círculo não pode ser exibido como asteriscos."

class Losango(Quadrilatero):
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return 4 * math.sqrt((self.base / 2)**2 + (self.altura / 2)**2)
    
    def exibir(self):
        lines = []
        for i in range(self.altura // 2 + 1):
            line = " " * (self.altura // 2 - i) + "*" * (i * 2 + 1)
            lines.append(line)
        for i in range(self.altura // 2):
            line = " " * i + "*" * (self.altura - 2 * i)
            lines.append(line)
        return "\n".join(lines)

class TipoTriangulo(ABC):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    @abstractmethod
    def verificar_triangulo(self):
        pass

class Equilatero(TipoTriangulo):
    def verificar_triangulo(self):
        return self.lado1 == self.lado2 == self.lado3

class Isosceles(TipoTriangulo):
    def verificar_triangulo(self):
        return self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3

class Escaleno(TipoTriangulo):
    def verificar_triangulo(self):
        return self.lado1 != self.lado2 != self.lado3

# Exemplos de uso
triangulo = Triangulo(5, 4)
print("Triângulo:")
print("Área:", triangulo.area())
print("Perímetro:", triangulo.perimetro())
print(triangulo.exibir())

quadrado = Quadrado(5, 5)
print("\nQuadrado:")
print("Área:", quadrado.area())
print("Perímetro:", quadrado.perimetro())
print(quadrado.exibir())

circulo = Circulo(3)
print("\nCírculo:")
print("Área:", circulo.area())
print("Perímetro:", circulo.perimetro())
print(circulo.exibir())

losango = Losango(7, 7)
print("\nLosango:")
print("Área:", losango.area())
print("Perímetro:", losango.perimetro())
print(losango.exibir())

triangulo_equilatero = Equilatero(5, 5, 5)
triangulo_isosceles = Isosceles(5, 5, 7)
triangulo_escaleno = Escaleno(3, 4, 5)

print("\nTipos de Triângulo:")
print("Equilátero:", triangulo_equilatero.verificar_triangulo())
print("Isósceles:", triangulo_isosceles.verificar_triangulo())
print("Escaleno:", triangulo_escaleno.verificar_triangulo())
