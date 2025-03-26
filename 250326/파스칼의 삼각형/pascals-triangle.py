n = int(input())
arr = [[0 for _ in range(i+1)] for i in range(n)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if j == 0 or i == j :
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for row in arr :
    for item in row :
        print(item, end=' ')
    print()