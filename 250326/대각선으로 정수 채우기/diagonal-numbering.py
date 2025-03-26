n, m = map(int, input().split())

# Please write your code here.
new_arr = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1

for lineno in range(n+m -1):
    for i in range(lineno+1):
        if i >= n or lineno-i >= m:
            continue
        new_arr[i][lineno-i] = cnt
        cnt += 1


for row in new_arr :
    for item in row :
        print(item, end=' ')
    print()
