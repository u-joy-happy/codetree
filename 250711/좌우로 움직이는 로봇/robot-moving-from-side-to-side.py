n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.

a, b = [], []

cur = 0
for i in range(n):
    for _ in range(t[i]):
        if d[i] == 'R': cur += 1
        else : cur -= 1
        a += [cur]

cur = 0
for i in range(m):
    for _ in range(t_b[i]):
        if d_b[i] == 'R': cur += 1
        else : cur -= 1
        b += [cur]

a_cur, b_cur = 0, 0
a_pre, b_pre = 0, 0
res = 0
for i in range(max(len(a), len(b))) :
    a_pre, b_pre = a_cur, b_cur

    if i >= len(a) : a_cur = a[-1]
    else : a_cur = a[i]
    
    if i >= len(b) : b_cur = b[-1]
    else : b_cur = b[i]

    if a_pre != b_pre and a_cur == b_cur :
        res += 1

print(res)
