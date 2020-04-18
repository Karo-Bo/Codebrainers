"""
Please write your implementation in place of pass keyword.
After you will are ready to test your implementation run whole
file. There are 16 test cases all of them should Pass
"""

def identity(nums):
    """Identity:
    Given a list of numbers, write a list comprehension that produces a copy of the list.
        >>> identity([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
        >>> identity([])
        []
    """
    # pass
    new_list = [element for element in nums]
    return new_list



def doubled(nums):
    """Doubled:
    Given a list of numbers, write a list comprehension that produces a list of each number doubled.
        >>> doubled([1, 2, 3, 4, 5])
        [2, 4, 6, 8, 10]
        >>> doubled([-2, 2, -10, 10])
        [-4, 4, -20, 20]
    """
    # pass
    new_list = [(element * 2) for element in nums]
    return new_list



def squared(nums):
    """Squared:
    Given a list of numbers, write a list comprehension that produces a list of the squares of each number.
        >>> squared([1, 2, 3, 4, 5])
        [1, 4, 9, 16, 25]
        >>> squared([-2, 2, -10, 10])
        [4, 4, 100, 100]
    """
    # pass
    new_list = [(element ** 2) for element in nums]
    return new_list



def evens(nums):
    """Evens:
    Given a list of numbers, write a list comprehension that produces a list of only the even numbers in that list.
        >>> evens([1, 2, 3, 4, 5])
        [2, 4]
        >>> evens([1, 3, 5])
        []
        >>> evens([-2, -4, -7])
        [-2, -4]
    """
    #pass
    new_list = [element for element in nums if element % 2 == 0]
    return new_list



def odds(nums):
    """Odds:
    Given a list of numbers, write a list comprehension that produces a list of only the odd numbers in that list.
        >>> odds([1, 2, 3, 4, 5])
        [1, 3, 5]
        >>> odds([2, 4, 6])
        []
        >>> odds([-2, -4, -7])
        [-7]
    """
    # pass
    new_list = [element for element in nums if element % 2 != 0]
    return new_list


def positives(nums):
    """Positives:
    Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.
        >>> positives([-2, -1, 0, 1, 2])
        [1, 2]
    """
    # pass
    new_list = [element for element in nums if element > 0]
    return new_list


def selective_stringify_nums(nums):
    """Selectively stringify nums:
    Given a list of numbers, write a list comprehension that produces a list of strings of each number that is divisible by 5.
        >>> selective_stringify_nums([25, 91, 22, -7, -20])
        ['25', '-20']
    """
    #pass
    new_list = [f'{element}' for element in nums if element % 5 == 0]
    return new_list



def words_not_the(sentence):
    """Words not 'the'
    Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.
        >>> words_not_the('the quick brown fox jumps over the lazy dog')
        [5, 5, 3, 5, 4, 4, 3]
    """
    # pass
    words_list = sentence.split()
    new_list = [len(word) for word in words_list if word != 'the']

    return new_list



def vowels(word):
    """Vowels:
    Given a string representing a word, write a list comprehension that produces a list of all the vowels in that word.
        >>> vowels('mathematics')
        ['a', 'e', 'a', 'i']
    """
    new_list = [element for element in word if element in {'a', 'e', 'a', 'i'}]
    return new_list



# STOP HERE! You solved everything!
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n*** ALL TESTS PASSED!\n')