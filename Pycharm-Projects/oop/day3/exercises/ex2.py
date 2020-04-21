import math


class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError

    def circumference(self):
        raise NotImplementedError


# Stworzyć klase Shape z metodami kostruktor, area, circumference )
# utworzyc klasy pochodne
# rectange, square, circle
# i odpowiednio je zaimplmentować

class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def area(self):  # nadpisanie metody
        return self.x * self.y

    def circumference(self):  # nadpisanie metody
        return 2 * (self.x + self.y)


class Square(Rectangle):
    def __init__(self, x):
        super().__init__(x, x)


class Circle(Shape):
    pi = math.pi

    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):  # nadpisanie metody
        return self.pi * self.r ** 2

    def circumference(self):  # nadpisanie metody
        return 2 * self.pi * self.r


shape_list = [Square(10), Rectangle(5, 10), Circle(10), Square(5)]
for shape in shape_list:
    print(shape.area(), shape.circumference())

print('----------')
rec = Rectangle(10, 20)
print(rec.circumference())
print(rec.area())
print('----------')
squ = Square(10)
print(squ.circumference())
print(squ.area())
print('----------')
cir = Circle(4)
print(cir.circumference())
print(cir.area())
print('----------')
#
# our_list = [[], [], []]
# for list in our_list:
#     list.append(10)
#
#     print(our_list)
