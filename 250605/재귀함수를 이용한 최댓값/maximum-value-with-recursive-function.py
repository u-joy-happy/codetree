n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def get_larger(n, m) :
    if m == len(arr) :
        return n
    if arr[n] > arr[m] :
        return get_larger(n, m+1)
    else : 
        return get_larger(m, m+1)

print(arr[get_larger(0, 1)])