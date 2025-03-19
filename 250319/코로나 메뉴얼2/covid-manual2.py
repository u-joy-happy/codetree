new_arr = [0] * 4

for _ in range(3) :
    a, b = input().split()
    b = int(b)
    if a == 'Y' and b >= 37 :
        new_arr[0] += 1
    elif a == 'N' and b >= 37 :
        new_arr[1] += 1
    elif a == 'Y' and b < 37 :
        new_arr[2] += 1
    else :
        new_arr[3] += 1

    # if b >= 37 :
    #     if a == 'Y' :
    #         new_arr[0] += 1
    #     else:
    #         new_arr[1] += 1
    # else :
    #     if a == 'Y' :
    #         new_arr[2] += 1
    #     else :
    #         new_arr[3] += 1

for a in new_arr :
    print(a, end=' ')

if new_arr[0] >= 2 :
    print('E')