n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def heap_sort(n):
    for i in range(n//2-1, -1, -1):
        heapify(i, n)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(0, i)

def heapify(i, n):
    largest = i
    l_child = i * 2 + 1
    r_child = i * 2 + 2

    if l_child < n and arr[l_child] > arr[largest]:
        largest = l_child
    if r_child < n and arr[r_child] > arr[largest]:
        largest = r_child

    if largest != i :
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(largest, n)

heap_sort(n)

for item in arr :
    print(item, end=' ')