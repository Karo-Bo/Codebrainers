def count_even_odd(collection):
    even = filter(lambda element: element % 2 == 0, collection)
    odd = filter(lambda element: element % 2 != 0, collection)

    return f'Even number = {len(list(even))}, odd number = {len(list(odd))}'

print(count_even_odd([1, 2, 3, 4, 5, 0, 8, 15, 16, 20]))