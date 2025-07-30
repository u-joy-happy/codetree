n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(n):
    min_val = i
    for j in range(i+1, n):
        if arr[min_val] > arr[j] :
            min_val = j
    arr[min_val], arr[i] = arr[i], arr[min_val]

for item in arr:
    print(item, end=' ')