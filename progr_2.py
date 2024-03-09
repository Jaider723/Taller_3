class Rectangulo:
    def __init__(self,alto,ancho):
        self.alto=alto
        self.ancho=ancho

    def rectangulo_ast(self):
        for i in range(self.alto):
            if i == 0 or i == self.alto - 1:
                for j in range(self.ancho):
                    print("*", end=" ")
                print()  
            else:
                print("*", end="")
                for j in range(self.ancho-2):
                    print(" ", end=" ")
                print(" *")  
    
    def calcular_area(self):
        area=self.alto*self.ancho
        return area

rectangulo = Rectangulo(5,10)
rectangulo.rectangulo_ast()
print(f"El area del rectangulo es {rectangulo.calcular_area()}")