from functools import reduce

temperatures = [10, 13, 14, 15, 14, 10]

acc = 1
for el in temperatures:
    acc = acc * el

print(acc)

acc2 = reduce(lambda elem1, elem2: elem1*elem2, temperatures)
print(acc2)


def a(arg1, arg2):
    with open(arg1, 'a') as f:
        # 'w', 'r', 'a'
        f.write(arg2)
    return(arg1, arg2)

a('plik.txt', "Nasz PLIK")
a('plik.txt', "Nasz PLIK")
a('plik.txt', "Nasz PLIK")
