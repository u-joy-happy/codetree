n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.

max_val = 0

for i in range(n):
    sum_val = 0
    for j in range(n):
        if x[i] <= x[j] <= x[i]+k:
            if c[j] == 'G':
                sum_val += 1
            elif c[j] == 'H':
                sum_val += 2
    max_val = max(max_val, sum_val)

print(max_val)
