def comparator(pair):
    return pair[0] + pair[1]


pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
pairs.sort(key=comparator, reverse=True)
print(pairs)