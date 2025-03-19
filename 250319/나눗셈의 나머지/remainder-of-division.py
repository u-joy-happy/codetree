a, b = map(int, input().split())

new_arr = [0] * b
tot = 0

while a > 1 :
    new_arr[a % b] += 1
    a //= b

for n in new_arr :
    tot += n ** 2 

print(tot)