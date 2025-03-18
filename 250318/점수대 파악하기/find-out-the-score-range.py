arr = map(int, input().split())
new_arr = [0] * 11

for a in arr :
    if a == 0 :
        break
    new_arr[a//10] += 1

for i in range(10, 0, -1) :
    print(f'{i*10} - {new_arr[i]}')