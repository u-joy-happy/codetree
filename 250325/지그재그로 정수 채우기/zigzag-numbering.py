n, m = map(int, input().split())

# Please write your code here.

new_arr = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0

for i in range(m):
    if i % 2 == 0 :
        for j in range(n):
            new_arr[j][i] = cnt
            cnt += 1
    else :
        for j in range(n-1, -1, -1):
            new_arr[j][i] = cnt
            cnt += 1

for row in new_arr :
    for item in row:
        print(item, end=' ')
    print()