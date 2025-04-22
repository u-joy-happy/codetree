n = input()
sum_val = 0

for item in n :
    if item >= '0' and item <= '9':
        sum_val += int(item)

print(sum_val)