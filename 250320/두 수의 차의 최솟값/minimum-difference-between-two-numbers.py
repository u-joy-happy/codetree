n = int(input())
arr = list(map(int, input().split()))

min_val = 100

for i in range(n) :
    for j in range(i+1,n):
        if arr[i] >= arr[j]:
            dist = arr[i] - arr[j]
        else :
            dist = arr[j] - arr[i]

        if dist < min_val :
            min_val = dist

print(min_val)