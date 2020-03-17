def average(collection):
    S = sum(collection)
    L = len(collection)
    return S/L

try:
    # print(average([]))
    print(average([1]))
    print(average([1, 2]))

except ZeroDivisionError:
    print("POWSTAŁ BŁĄD DZIELENIA PRZEZ ZERO!!!")
    # raise Exception("treść komunikatu")
    # powyższy błąd jako nie złapany wypisze Traceback

except (AttributeError, KeyError):
    print("POWSTAŁ BŁĄD DOSTĘPU")

else:
    print("Kod w try nie wywołał błędu")

finally: 
    print("Kod, który zawsze się wykona po try")

print("Dalsza część kodu")

# if zmienna_ma_zla_wartosc:
#     raise Exception("treść komunikatu")
    