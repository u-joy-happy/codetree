N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

a, b = [], []
for i in range(N):
    a += [v[i]] * t[i]
for i in range(M):
    b += [v2[i]] * t2[i]

a_sum, b_sum, res = 0, 0, 0
pre_first = ''

for i in range(len(a)):
    fisrt = ''
    a_sum += a[i]
    b_sum += b[i]

    if a_sum > b_sum:
        fisrt = 'a'
    elif a_sum < b_sum:
        fisrt = 'b'
    else :
        fisrt = 'both'
    
    if pre_first != fisrt :
        res += 1
        pre_first = fisrt

print(res)