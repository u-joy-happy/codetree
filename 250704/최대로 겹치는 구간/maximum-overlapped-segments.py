n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

offset = 0
max_x = 0

for a, b in segments :
    if a < offset :
        offset = a
    if b > max_x :
        max_x = b

arr = [0] * (max_x - offset)

for a, b in segments :
    a, b = a - offset, b - offset
    arr[a:b] = [arr[i] + 1 for i in range(a, b)]

print(max(arr))