ability = list(map(int, input().split()))

# Please write your code here.

ability.sort()
max_val = 0
min_val = 2 * 1000000

for i in range(3):
    val = ability[i] + ability[6-i-1]
    max_val = max(max_val, val)
    min_val = min(min_val, val)

print(max_val - min_val)