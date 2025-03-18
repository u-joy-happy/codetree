arr = map(int, input().split())

new_arr = [0] * 7

for a in arr :
    new_arr[a] += 1

for i in range(1, 7):
    print(f'{i} - {new_arr[i]}')