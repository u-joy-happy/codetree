N = int(input())
A = list(map(int, input().split()))

# Please write your code here.

cnt, res = 0, 0
max_val = 0

for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            print(i, j, k)

# print(res)