a, b = map(int, input().split())

print(a, b, sep=' ', end=' ')
for _ in range(3, 11) :
    a, b = b, (a + b) % 10
    print(b, end=' ')
