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

bad_cheese = []
for i in range(D):
    for j in range(S):
        if p[i] == sick_p[j] and t[i] < sick_t[j] :
            bad_cheese.append(m[i])

res = [0] * (N + 1)
for i in range(D):
    for j in range(S):
        if p[i] == sick_p[j] or m[i] in bad_cheese:
            res[p[i]] = 1

print(sum(res))