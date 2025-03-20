n = int(input())
arr = list(map(int, input().split()))

min_val = 100

for i in range(n-1) :
    dist = arr[i+1] - arr[i]
    if dist < min_val :
        min_val = dist

print(min_val)