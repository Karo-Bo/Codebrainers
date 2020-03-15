"""Weight-mean"""


def weight_mean(collection, weights):
    """Weighted arithmetic mean.

    As defined here:
    https://en.wikipedia.org/wiki/Weighted_arithmetic_mean
    """
    # The real issue here is how to iterate over
    # values in collection and weights at the same time.
    # It's required because we have to calculate
    #  value1*weight1 + value2*weight2 + ...
    # in the numerator.
    #
    # To achieve this: use zip(collection, weights)
    
    weight_sum = 0
    product_sum = 0

    for i, j in zip(collection, weights):
       product_sum += (i * j)
       weight_sum += j

    return product_sum / weight_sum


# TESTS!

from pytest import approx


def test_wm_simple():
    collection = [1, 1]
    weights = [0.5, 0.5]
    assert weight_mean(collection, weights) == 1.0


def test_wm_complex():
    collection = [62, 67, 71, 74, 76, 77, 78, 79, 79, 80, 80, 81, 81]
    weights = [0.3, 0.5, 0.1, 2, 3, 0.9, 1, 2, 1, 0.1, 0.5, 0.9, 1]
    assert weight_mean(collection, weights) == approx(76.797, 0.001)
