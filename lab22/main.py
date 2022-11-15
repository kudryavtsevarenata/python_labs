import sys
import json
sys.path.insert(0, './lab22/classes/')
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from circle import Circle

def write(data):
    jsonstr = json.dumps(data, indent = 4)
    open('./lab22/output.json', 'w').write(jsonstr)


def read_from_json():
    return json.load(open('./lab22/output.json', 'r'))


tr = Triangle(2, 3, 2)
c = Circle(56)
rec = Rectangle(8, 19)
sq1 = Square(50)
sq2 = Square(5)
l = [tr, c, rec, sq1, sq2]
data = {
    'amount' : len(l),
    'obj' : []
}
for elem in l:
    data['obj'].append(elem.__dict__)

write(data)
data.clear()
l.clear()
data = read_from_json()

for elem in data['obj']:
    if elem['name'] == "Triangle":
        obj = Triangle(elem['a'], elem['b'], elem['c'])
    elif elem['name'] == "Circle":
        obj = Circle(elem['r'])
    elif elem['name'] == "Rectangle":
        obj = Rectangle(elem['a'], elem['b'])
    elif elem['name'] == "Square":
        obj = Square(elem['a'])
    l.append(obj)
for elem in l:
    elem.draw()


