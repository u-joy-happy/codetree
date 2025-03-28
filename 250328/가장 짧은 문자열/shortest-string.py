max_len = 0
min_len = 20

for _ in range(3):
    a = input()
    if len(a) > max_len :
        max_len = len(a)
    if len(a) < min_len :
        min_len = len(a)

print(max_len - min_len)