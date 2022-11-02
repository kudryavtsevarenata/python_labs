import sys
import json
sys.path.append('./lab2/classes')
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from circle import Circle
l = []
with open('lab2/input.json', 'r') as file:
    data = json.load(file)
print(data)
for elem in data:
    if elem['name'] == "Triangle":
        t = Triangle(elem['size']['a'], elem['size']['b'], elem['size']['c'])
        l.append(t)
    elif elem['name'] == "Circle":
        c = Circle(elem['size']['r'])
        l.append(c)
    elif elem['name'] == "Rectangle":
        r = Rectangle(elem['size']['a'], elem['size']['b'])
        l.append(r)
    elif elem['name'] == "Square":
        s = Square(elem['size']['a'])
        l.append(s)

jsonstr = json.dumps(l[0].__dict__)
print(jsonstr)

with open('lab2/output.json', 'a') as file:
    file.write('[\n')
    for elem in l:
        if elem == l[-1]:
            jsonstr = json.dumps(elem.__dict__, indent=2)
            file.write(jsonstr)
        else:
            jsonstr = json.dumps(elem.__dict__, indent=2) + ',\n'
            file.write(jsonstr)
    file.write('\n]\n')




