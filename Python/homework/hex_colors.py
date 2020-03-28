def hexcolor(r, g, b):

    red = '{:02X}'.format(r)    
    green = '{:02X}'.format(g)
    blue = '{:02X}'.format(b)
        
    return "#" + red + green + blue

def validate(x):

    if (0 <= x <= 255):
        return True
    else:
        return False    

print("Podaj kolejne składowe koloru: ")
r = int(input("Podaj wartość składowej red: "))
g = int(input("Podaj wartość składowej green: "))
b = int(input("Podaj wartość składowej blue: "))

is_value_correct = True

for x in (r, g, b):
    if not (0 <= x <= 255):
        is_value_correct = False
        print(f"Podana składowa {x} jest niepoprawna")        

if is_value_correct == True:
    print("Kolor Hex dla tych składowych ma wartość: " + hexcolor(r, g, b))

def test_hexcolor():
    
    assert hexcolor(255, 99, 71) == "#FF6347"
    assert hexcolor(184, 134, 11) == "#B8860B"  
    assert hexcolor(189, 183, 107) == "#BDB76B"  
    assert hexcolor(0, 0, 205) == "#0000CD"  
