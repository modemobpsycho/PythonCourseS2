dict1 = {'x': 1}
dict2 = {'y': 2}
dict3 = {'x': 3, 'y': 4}

result = list(filter(lambda d: 'x' in d.keys(), [dict1, dict2, dict3]))
 
print(result)