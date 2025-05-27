A = input()

# Please write your code here.

diff = ord('z') - ord('a') + 1
arr = [ 0 for _ in range(diff)]

def is_exist(a) :
    for item in a :
        diff_val = ord(item) - ord('a')
        if arr[diff_val] == 0 :
            arr[diff_val] += 1
    
is_exist(A)

if sum(arr) >= 2 :
    print('Yes')
else :
    print('No')
