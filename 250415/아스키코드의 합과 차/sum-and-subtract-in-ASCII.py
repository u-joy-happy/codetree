a, b = input().split()

sum_val = ord(a) + ord(b)

if ord(a) > ord(b) :
    diff_val = ord(a) - ord(b)
else :
    diff_val = ord(b) - ord(a)


print(sum_val, diff_val)