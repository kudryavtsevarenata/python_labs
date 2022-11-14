from shape import Shape
import math

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.name = "Rectangle"
    
    def draw(self):
        print(f"Drawing rectangle with sides = {self.a}, {self.b}")
    
    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return 2 * self.a + 2 * self.b
    