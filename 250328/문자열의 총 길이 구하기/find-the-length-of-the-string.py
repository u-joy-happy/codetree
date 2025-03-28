arr = input().split()
cnt = 0

for i in range(len(arr)):
    cnt += len(arr[i])

print(cnt)