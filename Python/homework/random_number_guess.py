# pętla while:

import random

number = random.randint(1, 100)

i = 0
success = False

while (i < 7) and (success == False):
 
    user_number = int(input("Podaj liczbę: "))
    i += 1
    
    if user_number == number:
        print("Gratulacje, zgadłoś!")
        success = True

    elif user_number > number:
        print("Szukana liczba jest mniejsza")
        right_range = user_number - 1
        
    else:
        print("Szukana liczba jest większa")
        left_range = user_number + 1

if success == False:
    print("Nie zgadłoś!! :P") 

# ***************************
#
# pętla for:

# import random

# left_range = 1
# right_range = 100
# number = random.randint(left_range, right_range) 

# przy ostatnim zapytaniu podpowiada <39, 39> :P

# for i in range(0, 7):
#     user_number = int(input("Podaj liczbę z przedziału" +
#                             f"<{left_range}, {right_range}>"))

#     if user_number == number:
#         print("Gratulacje, zgadłoś!")
#         break

#     elif user_number > number:
#         print("Szukana liczba jest mniejsza")
#         right_range = user_number - 1
        
#     else:
#         print("Szukana liczba jest większa")
#         left_range = user_number + 1

#     if i == 6:
#         print("Looser")