n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

for i in range(n*2):
    for j in range(i+1, n*2):
        for k in range(j+1, n*2):
            if i < n : 
                f1, v1 = 'x', x[i]
            else : 
                f1, v1 = 'y', y[n-1]

            if j < n : 
                f2, v2 = 'x', x[j]
            else : 
                f2, v2 = 'y', y[j-n]

            if k < n : 
                f3, v3 = 'x', x[k]
            else : 
                f3, v3 = 'y', y[k-n]

            flag = True
            for l in range(n):
                if not ((x[l] == v1 and f1 == 'x') or (y[l] == v1 and f1 == 'y') or \
                (x[l] == v2 and f2 == 'x') or (y[l] == v2 and f2 == 'y') or \
                (x[l] == v3 and f3 == 'x') or (y[l] == v3 and f3 == 'y')) :
                    # print(f1, v1, f2, v2, f3, v3)
                    flag = False
                    break
            if flag :
                print(1)
                exit()
print(0)



