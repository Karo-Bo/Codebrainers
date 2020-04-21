class Door:
    def open(self):
        print(f'Open {self} of id: {id(self)}')


class Bottle:
    def open(self):
        print(f'Open {self} of id: {id(self)}')


class Window:
    def open(self):
        print(f'Open {self} of id: {id(self)}')


class File:
    def open(self):
        print(f'Open {self} of id: {id(self)}')

# id(self) id oznacza wewnętrzny numer w Pythonie oznaczający dany obiekt
door1 = Door()
door2 = Door()

print(id(door1))
print(id(door2))
print(door1 == door2)

things = [Door(), Bottle(), Window(), File()]
for thing in things:
    thing.open()