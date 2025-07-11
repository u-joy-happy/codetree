N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

vc = [0] * (N + 1)
res = [0] * (N + 1)

vc[P], res[P] = K, 1
handshakes.sort(key=lambda x: x[0])

for t, x, y in handshakes :
    if vc[x] and not res[y]:
        vc[x] = (max(vc[x]-1, 0))
        vc[y], res[y] = K, 1
    elif vc[y] and not res[x]:
        vc[y] = (max(vc[y]-1, 0))
        vc[x], res[x] = K, 1
    elif vc[x] or vc[y]:
        vc[x] = (max(vc[x]-1, 0))
        vc[y] = (max(vc[y]-1, 0))

for r in res[1:] :
    print(r, end='')
