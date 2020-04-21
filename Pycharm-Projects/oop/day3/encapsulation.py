class MyClass:
    _protected_class_attribute = 'ProtClassAttr'
    class_normal_attribute = 'NormalAttribute'

    def __init__(self):
        self.object_normal_attribute = None
        self._protected_attribute = None

    def public_method(self):
        self._private_method()  # in line with OOP Encapsulation principle
        print(f'Wywołałeś metodę publiczną {self._protected_attribute}')

    def _private_method(self):
        print('Wywołałeś metodę prywatną')

    def get_protected_attribute(self):
        return self._protected_attribute

    def set_protected_attribute(self, new_value):
        self._protected_attribute = new_value


x = MyClass()
print(x.object_normal_attribute)
print(MyClass.class_normal_attribute)
print(x.object_normal_attribute)
print(x._protected_attribute)  # violate OOP Encapsulation principle
print(MyClass._protected_class_attribute)  # As above
x.public_method()
x._private_method()  # violate OOP Encapsulation principle
# TypeError: public_method() takes 0 positional arguments but 1 was given

print(x.get_protected_attribute())
x.set_protected_attribute('Tadam')
print(x.get_protected_attribute())