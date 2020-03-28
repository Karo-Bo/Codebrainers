def integers_to_hexcolor(elements_list):

    return_string = "#"

    for element in elements_list:
        return_string += '{:02X}'.format(element)
        
    return return_string

def validate(x):

    if (0 <= x <= 255):
        return True
    else:
        return False

def read_user_input(color):

    temporary_value = int(input(f"Podaj wartość składowej {color}: "))

    while not validate(temporary_value):
        print("Podałeś niepoprawną wartość")
        temporary_value = int(input(f"Podaj wartość składowej {color}: "))

    return temporary_value

color_elements = []

print("Podaj kolejne składowe koloru: ")

for i in ("red", "green", "blue"):

    color_elements.append(read_user_input(i))    
        
print("Kolor Hex dla tych składowych ma wartość: " + integers_to_hexcolor(color_elements))
    