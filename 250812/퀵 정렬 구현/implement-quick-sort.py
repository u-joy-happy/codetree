n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def quick_sort(low, high) :
    if low < high :
        pos = partition(low, high)
        quick_sort(low, pos-1)
        quick_sort(pos+1, high)

def partition(low, high) :
    pivot = arr[high]
    x = low - 1

    for i in range(low, high):
        if arr[i] < pivot :
            x += 1
            arr[i], arr[x] = arr[x], arr[i]
    arr[x + 1], arr[high] = arr[high], arr[x + 1]
    return x + 1

quick_sort(0, n-1)

for item in arr :
    print(item, end=' ')