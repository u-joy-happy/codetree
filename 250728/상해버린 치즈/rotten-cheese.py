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

arr = [0] * (M + 1)
arr2 = [0] * (M + 1)
for i in range(D):
    for j in range(S):
        if p[i] == sick_p[j] and t[i] < sick_t[j] :
            arr[m[i]] += 1

for k in range(D):
    if arr[m[k]] == S:
        arr2[m[k]] += 1


print(max(arr2))

            