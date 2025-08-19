n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

res = 0
def check(max_val):
    idx_arr = []
    for idx, item in enumerate(arr):
        if item <= max_val :
            idx_arr.append(idx)
    
    for i in range(len(idx_arr)-1):
        if idx_arr[i+1] - idx_arr[i] > k :
            return False
    return True

for x in range(max(arr[0], arr[-1]), 101):
    if check(x) :
        res = x
        break

print(res)

