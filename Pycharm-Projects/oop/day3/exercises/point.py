class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        x_diff = self.x - other_point.x
        y_diff = self.y - other_point.y
        return (x_diff ** 2 + y_diff ** 2) ** 0.5

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y

    # redefiniowana domyślna metoda - operator porównania jeśli pomiędzy dwoma obiektami jest ==

    def __add__(self, other_point):
        new_x = self.x + other_point.x
        new_y = self.y + other_point.y
        return Point(new_x, new_y)

    def __str__(self):
        return f'Point: {self.x}, {self.y}'

    def __sub__(self, other_point):
        new_x = self.x - other_point.x
        new_y = self.y - other_point.y
        return Point(new_x, new_y)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("No such vector index")


point_a = Point(0, 0)
point_b = Point(1, 1)
point_c = Point(2, 1)
# print(point_a.distance(point_b))
# print(point_c.distance(point_b))
# print(point_b == point_c)
# print(point_b + point_c)
# print(point_b - point_c)
# print(point_b[0])
