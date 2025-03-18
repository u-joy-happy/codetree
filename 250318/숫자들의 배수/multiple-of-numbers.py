n = int(input())

cnt = 0
val = 0

while cnt < 2 :
    val += n
    print(val, end=' ')
    if val % 5 == 0 :
        cnt += 1