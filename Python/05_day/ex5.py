"""Factorial"""

# DONT USE factorial from math module

def factorial(n):
    """Recurive function used to calculate n!.

    n! is defined as: f(n) = 1*2*3*4*...*n
    https://en.wikipedia.org/wiki/Factorial
    """
    # if n <= 1:
    #     return 1
    # elif n > 1:
    #     return factorial(n-1) * n

    fact = 1        
    for i in range(1, n + 1):
        fact *= i

    return fact 



# TESTS!
#
###########
# CAUTION #
###########
# this time run tests with:
# pytest --tb=line ex5.py

def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial():
    assert factorial(6) == 720


def test_huge_factorial():
    """Ensure the function is not implemented using a recursion
    and can handle big numbers."""
    import sys
    assert factorial(sys.getrecursionlimit())
