input_cnt = 0
new_arr = []

while True :
    a = input()
    if a == '0':
        break

    input_cnt += 1
    if input_cnt % 2 == 1 :
        new_arr.append(a)

print(input_cnt)
print('\n'.join(new_arr))

    