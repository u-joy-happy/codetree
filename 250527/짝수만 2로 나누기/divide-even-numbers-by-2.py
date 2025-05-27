n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def div_even(arr, n):
    for i in range(n) :
        if arr[i] % 2 == 0 :
            arr[i] //= 2

div_even(arr, n)

for item in arr :
    print(item, end=' ')
            