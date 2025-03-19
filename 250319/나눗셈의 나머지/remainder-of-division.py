a, b = map(int, input().split())

new_arr = [0] * b
tot = 0

while True :
    new_arr[a % b] += 1
    a = a // b
    if a <= 1 :
        break

for n in new_arr :
    tot += n ** 2 

print(tot)