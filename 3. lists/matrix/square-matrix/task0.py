A = []
n, m = int(input()), int(input())
for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    A.append(row)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()
