def if_palindrome(collection):

    list_of_palindromes = list(filter(lambda x: x == x[::-1], collection))

    return list_of_palindromes

print(if_palindrome(['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa', 'kajak', 'kajok']))


# element = 'string'[::-1]
# print(element)