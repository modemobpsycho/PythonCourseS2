def summator(n):
    return sum([int(i) for i in str(n)])


numbers = [int(i) for i in input().split()]

print(*sorted(numbers, key=summator))
