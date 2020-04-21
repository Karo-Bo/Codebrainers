# class BaseClass:
#     pass
#
# class DerivedClass(BaseClass):
#     pass

class Base:
    def __init__(self):
        self.name = "Base"
        print('I am base class')

    def fun(self):
        print(f'Base class fun {self.name}')

b = Base()
b.fun()
print('--------------')

class Derived1(Base):
    def __init__(self):
        super().__init__() #- wywołanie konstruktora klasy bazowej
        # self.name = 'Derived' # jeśli tu nie jest 'nadpisana wartość' to przyjmie klasy nadrzędnej
        print('I am derived class One')

    def not_so_funny(self):
        print('Name is undefined')

class Derived2(Base):
    def __init__(self):
        super().__init__()
        print('I am derived class Two')
        # super().fun() # wywołanie metody z klady nadrzędnej/bazowej
    def fun(self): # overriden method
        print('Overridden method')

d = Derived1()
d.fun()
d.not_so_funny()

