a, b = map(int, input().split())
new_num = str(a + b)

cnt_val = 0

for item in new_num :
    if item == '1' :
        cnt_val += 1

print(cnt_val)
