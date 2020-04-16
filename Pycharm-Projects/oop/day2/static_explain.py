# counter = 0

class Point:
    # statyczne atrybuty
    _counter = 0

    def __init__(self, x, y):
        # self._counter += 1
        Point._counter += 1
        # global counter
        # counter += 1
        self.x = x  # pole o nazwie x, które jak stworzymy obiekt, przyjmie wartość x podaną w kontruktorze
        self.y = y

    def __str__(self):  # metoda magiczna
        return f'Point: {self.x}, {self.y} z {self._counter}'

    def __del__(self):
        Point._counter -= 1

    @staticmethod
    def description():
        print('This is 2d Point. Future work to be done')

    @staticmethod
    def increase_counter():
        Point._counter += 1


first_point = Point(10, 20)
print(first_point)

second_point = Point(10, 30)
third_point = Point(10, 30)

print(Point._counter)
print(first_point._counter)
# print(counter)

del first_point
print(Point._counter)

Point.increase_counter()
print(Point._counter)

Point.description()
second_point.description()
