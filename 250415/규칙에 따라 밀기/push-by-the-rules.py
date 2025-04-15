a = input()
q = input()

l_cnt = q.count('L')
r_cnt = q.count('R')
cnt = 0

if l_cnt > r_cnt :
    cnt = l_cnt - r_cnt
    a = a[cnt:] + a[:cnt]
elif r_cnt > l_cnt :
    cnt = r_cnt - l_cnt
    a = a[-cnt:] + a[:-cnt] 

print(a)



