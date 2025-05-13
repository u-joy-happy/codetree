n, a = input().split()
n = int(n)

match_cnt = 0

for _ in range(n):
    s = input()
    if a == s :
        match_cnt += 1

print(match_cnt)
