list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

result = 0
for x, y in zip(list1, list2):
    result += x*y
print(result)