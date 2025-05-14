a, b = map(int, input().split())

res = str(a//b) + '.'

for _ in range(20):
    a %= b
    a *= 10
    res += str(a//b)

print(res)
