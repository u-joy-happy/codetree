n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.

def check(i):
    for j in range(n):
        if a[j] <= i * (2**(j+1)) <= b[j]:
            continue
        else :
            return False
    return True

res = 0
for i in range(1, 5000):
    if check(i):
        res = i
        break

print(res)