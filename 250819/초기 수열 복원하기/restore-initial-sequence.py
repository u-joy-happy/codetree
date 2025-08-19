n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.

def check(arr) :
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return False
    return True

for a in range(1, adjacent[0]) :
    new_arr = []
    val = a
    new_arr.append(val)
    for i in range(n-1):
        val = adjacent[i] - val
        new_arr.append(val)
    
    if check(new_arr) :
        for item in new_arr:
            print(item, end=' ')
        break