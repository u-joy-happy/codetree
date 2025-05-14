same_val = -1
a = input()
b = input()

for i in range(len(a)):
    a = a[-1:] + a[:-1]
    if a == b :
        same_val = i + 1
        break

print(same_val)