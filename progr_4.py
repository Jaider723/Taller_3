import math

class Calculadora_Cientifica:
    def __init__(self,marca = "CASIO"):
        self.marca=marca
    
    def suma(self, x, y):
        return x+y
    
    def resta(self, x, y):
        return x-y
    
    def multiplicacion(self, x, y):
        return x*y
    
    def division(self, x, y):
        if y==0:
            return "Error: División por cero"
        else:
            return x/y
    
    def potencia(self, x, y):
        return x**y
    
    def raiz_cuadrada(self, x):
        if x < 0:
            return "Error: No se puede calcular la raíz cuadrada de un número negativo"
        else:
            return math.sqrt(x)
    
    def seno(self, x):
        return math.sin(x)
    
    def coseno(self, x):
        return math.cos(x)
    
    def tangente(self, x):
        return math.tan(x)
    
    def logaritmo(self, x, base=10):
        if x <= 0:
            return "Error: No se puede calcular el logaritmo de un número menor o igual a cero"
        else:
            return math.log(x, base)
    
    def factorial(self, x):
        if x < 0:
            return "Error: No se puede calcular el factorial de un número negativo"
        elif x == 0:
            return 1
        else:
            return math.factorial(x)

calculadora = Calculadora_Cientifica()
print("Suma:", calculadora.suma(5, 3))
print("Resta:", calculadora.resta(5, 3))
print("Multiplicación:", calculadora.multiplicacion(5, 3))
print("División:", calculadora.division(5, 3))
print("Potencia:", calculadora.potencia(5, 3))
print("Raíz Cuadrada:", calculadora.raiz_cuadrada(9))
print("Seno:", calculadora.seno(math.pi/2))
print("Coseno:", calculadora.coseno(math.pi))
print("Tangente:", calculadora.tangente(math.pi/4))
print("Logaritmo:", calculadora.logaritmo(100))
print("Factorial:", calculadora.factorial(5))
