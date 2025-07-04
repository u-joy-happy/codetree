n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_x = 0

for a, b in segments :
    if b > max_x :
        max_x = b

arr = [0] * max_x


for a, b in segments :
    for i in range(a-1, b):
        arr[i] += 1

print(max(arr))
