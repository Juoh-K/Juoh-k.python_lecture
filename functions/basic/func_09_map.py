## map function

def add_1(n) :
    return n + 1

target = [1, 2, 3, 4, 5]
result = []

# for value in target :
#     result.append(add_1(value))

result = list(map(add_1, target))

print(result)

