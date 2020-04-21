def find_numbers(collection):
    devisible_by_nineteen = filter(lambda x: x % 19 == 0, collection)
    devisible_by_thirteen = filter(lambda x: x % 13 == 0, collection)

    return list(devisible_by_nineteen), list(devisible_by_thirteen)


print(find_numbers([1, 13, 19, 30, 26, 90, 190, 260, 38]))
