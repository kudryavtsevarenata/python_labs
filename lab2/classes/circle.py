from shape import Shape
import math

class Circle(Shape):

    def __init__(self, r):
        self.r = r
    
    def draw(self):
        print(f"Drawing circle with radius = {self.r}")
    
    def area(self):
        return math.pi * self.r ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.r
    