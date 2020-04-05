# funkcja usuwająca zera z listy 

def remove_zeros(given_list):

    list_without_zero = []

    for element in given_list:
        if element != 0:
            list_without_zero.append(element)

    return list_without_zero

# funkcja sortująca listę

def sort_desc(given_list):

    # sorted_list = []
    
    # for i in range(0, len(given_list)):
    #     for element in given_list:
    #         if element == max(given_list):
    #             sorted_list.append(element)
    #             given_list.remove(element)  

    return sorted(given_list, key=None, reverse=True)

# funkcja sprawdzająca czy iilość elementów jest mniejsza od danej wartości
# zwraca wartość logiczną danego wyrażenia

def length_check(n, given_list):

    return n > len(given_list)

# funkcja odejmująca 1 od pierwszych n-elementów listy

def substract_one_for_n_elements(n, given_list):

    minus_one_list = given_list[:]

    for i in range(0, n):
        minus_one_list[i] -= 1

    return minus_one_list

# wielki finał i kompletny algorytm Havel-Hakimi.
# This algorithm will return true if the answers are consistent 
# (i.e. it's possible that everyone is telling the truth) 
# and false if the answers are inconsistent (i.e. someone must be lying)

def hh(given_list):

    if given_list == []:
        return True
        
    else:
        # 1
        while given_list != []:
            given_list = remove_zeros(given_list)
        # 2
            if given_list == []:
                return True
                break

            else:
        # 3
                given_list = sort_desc(given_list)
        # 4
                n = given_list.pop(0)          
        # 5         
                if length_check(n, given_list):
                    return False
                    break
        # 6, 7
                else:
                    given_list = substract_one_for_n_elements(n, given_list)                

# *****************************************
# testy


def test_remove_zeros():

    assert remove_zeros([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]) == [5, 3, 2, 6, 2, 7, 2, 5]
    assert remove_zeros([4, 0, 0, 1, 3]) == [4, 1, 3]
    assert remove_zeros([1, 2, 3]) == [1, 2, 3]
    assert remove_zeros([0, 0, 0]) == []
    assert remove_zeros([]) == []


def test_sort_desc():

    assert sort_desc([5, 1, 3, 4, 2]) == [5, 4, 3, 2, 1]
    assert sort_desc([0, 0, 0, 4, 0]) == [4, 0, 0, 0, 0]
    assert sort_desc([1]) == [1]
    assert sort_desc([]) == []


def test_length_check():

    assert length_check(7, [6, 5, 5, 3, 2, 2, 2]) is False
    assert length_check(5, [5, 5, 5, 5, 5]) is False
    assert length_check(5, [5, 5, 5, 5]) is True
    assert length_check(3, [1, 1]) is True
    assert length_check(1, []) is True
    assert length_check(0, []) is False


def test_substract_one_for_n_elements():

    assert substract_one_for_n_elements(4, [5, 4, 3, 2, 1]) == [4, 3, 2, 1, 1]
    assert substract_one_for_n_elements(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]) == [13, 12, 12, 12, 11, 9, 7, 7, 6, 6, 5, 6, 4, 4, 2]
    assert substract_one_for_n_elements(1, [10, 10, 10]) == [9, 10, 10]
    assert substract_one_for_n_elements(3, [10, 10, 10]) == [9, 9, 9]
    assert substract_one_for_n_elements(1, [1]) == [0]


def test_hh():

    assert hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]) is False
    assert hh([4, 2, 0, 1, 5, 0]) is False
    assert hh([3, 1, 2, 3, 1, 0]) is True
    assert hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]) is True
    assert hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]) is True
    assert hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]) is False
    assert hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]) is False
    assert hh([2, 2, 0]) is False
    assert hh([3, 2, 1]) is False
    assert hh([1, 1]) is True
    assert hh([1]) is False
    assert hh([]) is True
