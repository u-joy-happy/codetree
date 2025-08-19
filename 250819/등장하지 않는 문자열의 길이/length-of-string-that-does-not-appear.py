N = int(input())
str = input()

# Please write your code here.

max_len = 0
for i in range(N):
    for j in range(i+1, N+1):
        for k in range(i+1, N):
            for l in range(k+1, N+1):
                if str[i:j] == str[k:l]:
                    max_len = max(max_len, j-i)

print(max_len +1)