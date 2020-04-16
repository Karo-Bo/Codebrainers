class Rectangle:
    def __init__(self, side_a, side_b):
        self.length = side_a
        self.width = side_b

    def rectangle_area(self):
        return self.length * self.width

rect1 = Rectangle(2, 3)
print(rect1.rectangle_area())