arr = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        if i == 0 or j == 0 :
            arr[i][j] = 1
            continue    
        arr[i][j] = arr[i-1][j] + arr[i][j-1]
    
for row in arr :
    for item in row :
        print(item, end=' ')
    print()