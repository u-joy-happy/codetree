n = int(input())
S = input()

# Please write your code here.

cnt = 0
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if S[i] == 'C' and S[j] == 'O' and S[k] == 'W':
                cnt += 1
print(cnt)