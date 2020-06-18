def find_max_binary_gap(N):

    # binary_list = []
    current_gap = 0
    maximum_gap = 0

    while N > 0 and N % 2 == 0:
        N = N // 2

    while N > 0:
        if N % 2 == 0:
            current_gap += 1
            maximum_gap = max(maximum_gap, current_gap)
        else:
            current_gap = 0
        N = N // 2

    return maximum_gap

print(find_max_binary_gap(1041))
print(find_max_binary_gap(2172))
print(find_max_binary_gap(15))
print(find_max_binary_gap(32))
print(find_max_binary_gap(591))

# def change_into_binary_list(N):
#     binary_list = []

#     while N > 0:

#         binary_list.append(N % 2)
#         N = N // 2

#     return binary_list


# # print(change_into_binary_list(2172))


# def max_zeros_count(binary_list):
#     current_gap = 0
#     maximum_gap = 0

#     for i in range(len(binary_list)):

#         if binary_list[i] == 1:

#                 for j in range(len(binary_list)-i):

#                     if binary_list[i + j] == 0:

#                         current_gap += 1
#                         maximum_gap = max(maximum_gap, current_gap)

#                     else:
#                         current_gap = 0

#     return maximum_gap


# def find_max_binary_gap(N):
#     binary_gap = max_zeros_count(change_into_binary_list(N))

#     return binary_gap


# print(find_max_binary_gap(1041))
# print(find_max_binary_gap(2172))
# print(find_max_binary_gap(15))
# print(find_max_binary_gap(32))
# print(find_max_binary_gap(591))