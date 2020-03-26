def hexcolor(r, g, b):

    if 0 <= r <= 9:
        red = "0" + str(r)
    elif 9 < r < 16:
        red = "0" + format(r, 'X')
    else:
        red = format(r, 'X')

    if 0 <= g <= 9:
        green = "0" + str(g)
    elif 9 < g < 16:
        green = "0" + format(g, 'X')
    else:
        green = format(g, 'X')

    if 0 <= b <= 9:
        blue = "0" + str(b)
    elif 9 < b < 16:
        blue = "0" + format(b, 'X')
    else:
        blue = format(b, 'X')
    
    return "#" + red + green + blue

print("Podaj kolejne składowe koloru: ")
r = int(input("Podaj wartość składowej red: "))
g = int(input("Podaj wartość składowej green: "))
b = int(input("Podaj wartość składowej blue: "))

print("Kolor Hex dla tych składowych ma wartość: " + hexcolor(r, g, b))

def test_hexcolor():
    
    assert hexcolor(255, 99, 71) == "#FF6347"
    assert hexcolor(184, 134, 11) == "#B8860B"  
    assert hexcolor(189, 183, 107) == "#BDB76B"  
    assert hexcolor(0, 0, 205) == "#0000CD"  
