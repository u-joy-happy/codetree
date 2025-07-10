n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

# MAX_V = 1000000 + 1
# at, bt = [0] * MAX_V, [0] * MAX_V
at, bt = [], []

for i in range(n):
    at += [v[i]] * t[i]

for i in range(m):
    bt += [v2[i]] * t2[i]

a_sum, b_sum = 0, 0
res = 0
first = ''

for i in range(len(at)) :
    a_sum += at[i]
    b_sum += bt[i]

    if a_sum == b_sum :
        continue
        
    tmp = first
    first = 'a' if a_sum > b_sum else 'b'
    if tmp != first : res += 1

print(res-1)
