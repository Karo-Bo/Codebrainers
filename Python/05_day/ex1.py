r"""Length of the hypotenuse

In geometry, a hypotenuse is the longest side of a right-angled triangle,
the side opposite the right angle.

   this is hypotenuse
|\
| \
+--

"""


def hypotenuse(side_a, side_b):
    side_c = (side_a ** 2 + side_b ** 2) ** 0.5
    return side_c






# TESTS!
# To ensure our function is working properly, we should write tests that will
# exam function's output and input parameters.

# 1. install `pytest` with `pip install pytest`
# 2. run below tests with `pytest ex1.py`

def test_pythagorean_triple():
    assert hypotenuse(3, 4) == 5

    # make sure it's no difference when the sides are switched
    assert hypotenuse(4, 3) == 5

    # failure
    assert hypotenuse(1, 2) == 5 ** 0.5


# Pytest discovers functions that start with `test_` or end with `_test`
# and plugs into Python's `assert` statement to provide us with richer output
# (including coloring :) ).


# We shouldn't only check the obvious cases when the function works correctly.
# But in this case any correct input will work just fine.
