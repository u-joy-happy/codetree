n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

arr = [0] * n

for i in range(k):
    for idx in range(commands[i][0]-1,commands[i][1]):
        arr[idx] += 1

print(max(arr))