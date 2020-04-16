class Circle:
    def __init__(self, r):
        self.radius = r

    def circle_area(self):
        return(3.14 * self.radius ** 2)

    def circle_perimeter(self):
        return(2 * 3.14 * self.radius)

circle1 = Circle(5)
print(circle1.circle_area())
print(circle1.circle_perimeter())