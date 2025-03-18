arr = map(int, input().split())

res = 0
for i in arr :
    if i % 3 == 0 :
        print(res)
        break
    res = i