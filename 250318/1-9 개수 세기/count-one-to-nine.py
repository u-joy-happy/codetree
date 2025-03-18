n = int(input())
arr = map(int, input().split())

new_arr = [0] * 10

for a in arr :
    new_arr[a] += 1

for a in new_arr[1:] :
    print(a)