arr = map(int, input().split())

new_arr = [0] * 10
for a in arr :
    if a == 0 :
        break
    new_arr[a//10] += 1

for i in range(1, 10) :
    print(f'{i} - {new_arr[i]}')