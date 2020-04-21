def square_cube(collection):

    new_list = map(lambda element: f'({element ** 2}, {element ** 3})', collection)
    return new_list

print(list(square_cube([1, 2, 3, 4, 5, 0])))