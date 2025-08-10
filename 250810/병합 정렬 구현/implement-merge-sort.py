n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
res_arr = [0] * n

def merge_sort(low, high):
    if low < high :
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid +1, high)
        merge(low, mid, high)

def merge(low, mid, high):
    i, j = low, mid + 1
    k = low
    while i <= mid and j <= high :
        if arr[i] <= arr[j]:
            res_arr[k] = arr[i]
            k += 1
            i += 1
        else :
            res_arr[k] = arr[j]
            k += 1
            j += 1
        
    while i <= mid :
        res_arr[k] = arr[i]
        k += 1
        i += 1
    
    while j <= high :
        res_arr[k] = arr[j]
        k += 1
        j += 1
    
    for idx in range(low, high + 1):
        arr[idx] = res_arr[idx]

merge_sort(0, n-1)
for item in arr :
    print(item, end=' ')