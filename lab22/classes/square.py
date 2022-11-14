from shape import Shape
import math

class Square(Shape):

    def __init__(self, a):
        self.a = a
        self.name = "Square"
    
    def draw(self):
        print(f"Drawing square with side = {self.a}")
    
    def area(self):
        return self.a ** 2
    
    def perimeter(self):
        return 4 * self.a
    