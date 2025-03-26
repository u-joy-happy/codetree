n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
val = 1

for i in range(n-1, -1, -1):
    if (i % 2 == 0 and n % 2 == 0) or (i % 2 == 1 and n % 2 == 1) :
        for j in range(n):
            arr[j][i] = val
            val += 1
    else :
        for j in range(n-1, -1, -1):
            arr[j][i] = val
            val += 1

for row in arr:
    for item in row:
        print(item, end=' ')
    print()