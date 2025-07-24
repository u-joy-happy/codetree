N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.

def in_range(x, a):
    min_range, max_range = a, a
    pwd_range = [a]

    for _ in range(2):
        min_range -= 1
        if min_range == 0:
            min_range = N
        pwd_range.append(min_range)
    for _ in range(2):
        max_range += 1
        if max_range == N+1 :
            max_range = 1
        pwd_range.append(max_range)

    if x in pwd_range:
        return True
    return False

res = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if in_range(i, a1) and in_range(j, b1) and in_range(k, c1) \
                or in_range(i, a2) and in_range(j, b2) and in_range(k, c2) :
                res += 1

print(res)