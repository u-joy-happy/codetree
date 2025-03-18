a, b = map(int, input().split())

print(a, b, sep=' ', end=' ')
for _ in range(3, 11) :
    a, b = b, a*2 + b
    print(b, end=' ')