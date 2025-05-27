n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def get_abs_array(arr, n) :
    for i in range(n) :
        if arr[i] < 0 :
            arr[i] = -arr[i]

get_abs_array(arr, n)

for item in arr :
    print(item, end=' ')