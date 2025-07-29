N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.

# 상한 치즈 구하기 
per_arr = []
for i in range(S):
    sick_ch = [0] * (M+1)
    for j in range(D):
        if p[j] == sick_p[i] and t[j] < sick_t[i]:
            sick_ch[m[j]] = 1
    per_arr.append(sick_ch)

cheese_arr = []
for i in range(M+1):
    flag = True
    for j in range(S):
        if per_arr[j][i] == 0:
            flag = False
            break
    if flag : cheese_arr.append(1)
    else : cheese_arr.append(0)

# 상한 치즈 먹은 사람 구하기
max_val = 0
for i in range(1, M+1):
    res_arr = [0] * (N + 1)
    for j in range(D):
        if m[j] == i and cheese_arr[i] == 1 :
            res_arr[p[j]] = 1
    max_val = max(max_val, sum(res_arr))

print(max_val)