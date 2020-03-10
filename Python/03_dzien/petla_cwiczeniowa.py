for a in range(1, 101):
    if a % 15 == 0:
        print(f"{a} FizzBuzz")
    elif a % 3 == 0:
        print(f"{a} Fizz")
    elif a % 5 == 0:
        print(f"{a} Buzz")
    else:
        print(a)

# for a in range(1, 101):
#     if a % 3 == 0 and a % 5 != 0:
#         print(a, "Fizz")
#     elif a % 5 == 0 and a % 3 != 0:
#         print(a, "Buzz")
#     elif a % 15 == 0:
#         print(a, "FizzBuzz")
#     else:
#         print(a)

