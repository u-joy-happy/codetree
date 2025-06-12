n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

new_arr = []

def get_mid():
    new_arr.sort()
    print(new_arr[len(new_arr)//2], end=' ')

for i in range(n) :
    new_arr.append(arr[i])
    if i % 2 == 0:
        get_mid()

