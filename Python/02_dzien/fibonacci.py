
# ZADANIE
# wartość n-tego wyrazu ciągu Fibonacciego, wynik pokazywany na ekranie
# n = 10  F(10)
# 2. lista (.append() - na koniec dodaje nowy wyraz ciągu)
# 3*. rekurencja

# *******************************
# 1. zmienne które trzymają poprzednie wartości

# elementIndex = 12
# elementNMinusTwo = 0
# elementNMinusOne = 1

# if elementIndex < 1:
#     print("Nieprawidłowa wartość")
# elif elementIndex == 1:
#     print(elementNMinusTwo)
# elif elementIndex == 2:
#     print(elementNMinusOne)
# else:
#     for n in range(3, elementIndex + 1):
#         elementN = elementNMinusTwo + elementNMinusOne
#         elementNMinusTwo = elementNMinusOne
#         elementNMinusOne = elementN
#     print(elementN)

# *************************************
# 2. lista (.append() - na koniec dodaje nowy wyraz ciągu)

elementIndex = 10
fibonacci = [0, 1]

if elementIndex < 1:
    print("Nieprawidłowa wartość")
elif elementIndex == 1:
    print(fibonacci[0])
elif elementIndex == 2:
    print(fibonacci[1])
else:
    for n in range(2, elementIndex): # zasięg spójny z indeksami w liście
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    print(fibonacci[-1])
    