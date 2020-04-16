list = tuple

a = [1,2,3,4,5]
print(tuple(a))
print(list(a))

# dlaczego??

a = (1,2,3)
b = [1,2,3]
print(list(a))
print(b)
print(list(b))
print(tuple(b))