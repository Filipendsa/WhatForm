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
        return "\n".join(["*" * (i + 1) for i in range(int(self.altura))])


class Quadrado(Quadrilatero):
    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 4 * self.base

    def exibir(self):
        return "\n".join(["*" * int(self.base)] * int(self.altura))


class Retangulo(Quadrilatero):
    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def exibir(self):
        return "\n".join(["*" * int(self.base)] * int(self.altura))


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
        for i in range(int(self.altura) // 2 + 1):
            line = " " * (int(self.altura) // 2 - i) + "*" * (i * 2 + 1)
            lines.append(line)
        for i in range(int(self.altura) // 2):
            line = " " * i + "*" * (int(self.altura) - 2 * i)
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


def criar_forma():
    print("Escolha uma forma geométrica:")
    print("1. Triângulo")
    print("2. Quadrado")
    print("3. Retângulo")
    print("4. Círculo")
    print("5. Losango")

    escolha = int(input("Digite o número da forma desejada: "))

    if escolha == 1:
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        return Triangulo(base, altura)
    elif escolha == 2:
        lado = float(input("Digite o lado do quadrado: "))
        return Quadrado(lado, lado)
    elif escolha == 3:
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        return Retangulo(base, altura)
    elif escolha == 4:
        raio = float(input("Digite o raio do círculo: "))
        return Circulo(raio)
    elif escolha == 5:
        diagonal_maior = float(input("Digite a diagonal maior do losango: "))
        diagonal_menor = float(input("Digite a diagonal menor do losango: "))
        return Losango(diagonal_maior, diagonal_menor)
    else:
        print("Opção inválida.")


forma = criar_forma()
print("Área:", forma.area())
print("Perímetro:", forma.perimetro())
print(forma.exibir())
