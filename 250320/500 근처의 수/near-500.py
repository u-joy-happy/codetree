arr = list(map(int, input().split()))

max_val = 0
min_val = 1000

for n in arr :
    if n >= max_val and n < 500 :
        max_val = n
    elif n <= min_val and n > 500 :
        min_val = n

print(max_val, min_val)