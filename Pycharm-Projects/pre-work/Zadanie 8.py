a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 23, 26]
b = []
x = int(input('Podaj wartość x: '))
# if a != []:
for element in a:
    if element < x:
        # print(f'{element}, ', end ='')
# 8a
        b.append(element)
# 8b
print(b)