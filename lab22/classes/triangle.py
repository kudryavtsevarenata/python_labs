from shape import Shape
import math

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = "Triangle"
    
    def draw(self):
        print(f"Drawing triangle with sides = {self.a}, {self.b}, {self.c}")
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c
    