n, q = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(q):
    cond = list(map(int, input().split()))

    if cond[0] == 1 :
        print(arr[cond[1]-1])
    elif cond[0] == 2 :
        if cond[1] in arr :
            print(arr.index(cond[1]) +1)
        else :
            print(0)
    elif cond[0] == 3 :
        for a in arr[cond[1]-1:cond[2]]:
            print(a, end=' ')
        print()