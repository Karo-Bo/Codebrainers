from typing import Dict

our_dict = {1: "1", 2: "2", 3: "3"}
list_one = [1, 2, 3, 0, 100]
list_two = ['1', '2', '3', '0', 'as']

print(dict(zip(list_one, list_two)))

list_of_tuples = [(1, 1), (2, 2)]
print(dict(list_of_tuples))

list_three = [1, 2]  # weźmie tylko tyle elementów ile jest w "mniejszej" liście
print(list(zip(list_one, list_three)))

# Dictionary comprehension

dict_from_zip = dict(zip(list_one, list_two))

print(dict_from_zip.items())

x = {k * 10: v for (k, v) in dict_from_zip.items() if k < 3 and v > '1'}
print(x)

# dict_compre = {x: x for our_dict}

accounts = {'Artur': 10, 'Karolina': 1000, 'Michal': 1000}

new_accounts = {
    name: balance * 1.1 for (name, balance) in accounts.items() # if coś tam
}

print(new_accounts)
