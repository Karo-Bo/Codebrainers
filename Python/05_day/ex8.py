from math import floor

def tax(income):

    if income < 10e3:
        return 0

    elif income < 30e3:
        return int((income - 10e3) * 0.1)

    elif income < 100e3:
        return floor(19999 * 0.1 + (income - 30e3) * 0.25)

    else:
        return floor(19999 * 0.1 + 69999 * 0.25 + (income - 100e3) * 0.4)

    
def test_tax():
    assert tax(0) == 0
    assert tax(10000) == 0
    assert tax(10009) == 0
    assert tax(10010) == 1
    assert tax(12000) == 200
    assert tax(56789) == 8697
    assert tax(1234567) == 473326