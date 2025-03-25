n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        arr[i][j] = (i*m)+(j+1)


for row in arr :
    for item in row :
        print(item, end=' ')
    print()