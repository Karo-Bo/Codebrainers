def mean(collection):
    numerator = sum(collection)
    denominator = len(collection)
    return numerator / denominator

result = mean([1, 2, 3])
print(result)
