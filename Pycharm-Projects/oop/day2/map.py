accounts = {'Artur': 10, 'Karolina': 1000, 'Michal': 1000}

new_accounts = {
    name: balance * 1.01 for (name, balance) in accounts.items()  # if coś tam
}

print(new_accounts)

new_accounts2 = map(lambda items: (items[0], items[1] * 1.01), accounts.items())

print(dict(new_accounts2))

x = list(range(0, 31))

x_squared = list(map(lambda element: element ** 2, x))
print(x_squared)


def make_square(element):
    return element ** 2


x_squared2 = list(map(make_square, x))
print(x_squared2)
