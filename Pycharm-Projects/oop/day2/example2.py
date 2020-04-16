import statistics

temperatures = [10, 12, 14, 15, 10, 9, 5]

high_temperatures = [
    x for x in temperatures if x > 12
]

print(high_temperatures)

above_medium = [
    x for x in temperatures if x > statistics.mean(temperatures)
]

print(above_medium)

under_medium = list(filter(lambda x: x < statistics.mean(temperatures), temperatures))

# def if_greater_than_mean(x):
#     if x > statistics.mean(temperatures):
#         return True
#     else:
#         return False
# under_medium = list(filter(if_greater_than_mean, temperatures))

print(under_medium)

