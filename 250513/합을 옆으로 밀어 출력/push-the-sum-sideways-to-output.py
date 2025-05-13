n = int(input())
sum_val = 0

for _ in range(n) :
    sum_val += int(input())

new_str = str(sum_val)
new_int = new_str[1:] + new_str[:1]

print(new_int)
