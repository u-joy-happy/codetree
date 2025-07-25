n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.

def check(num1, num2, cnt1, cnt2):
    if cnt1 == 0 and cnt2 == 0 :
        return False
    n1 = []
    n2 = []
    for i in range(3):
        n1.append(num1 % 10)
        n2.append(num2 % 10)
        num1 //= 10
        num2 //= 10

    if cnt1 > 0 :
        s_cnt = 0
        if n1[0] == n2[0] : s_cnt += 1
        if n1[1] == n2[1] : s_cnt += 1
        if n1[2] == n2[2] : s_cnt += 1
        if s_cnt != cnt1 : 
            return False
    if cnt2 > 0 :
        b_cnt = 0
        if n1[0] == n2[1] or n1[0] == n2[2] : b_cnt +=1
        if n1[1] == n2[0] or n1[1] == n2[2] : b_cnt +=1
        if n1[2] == n2[0] or n1[2] == n2[1] : b_cnt +=1
        if b_cnt != cnt2 :
            return False
    return True

res = 0
for i in range(1,10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k :
                continue
            num = (i * 100) + (j * 10) + k
            flag = True
            for l in range(n):
                if not check(num, a[l], b[l], c[l]):
                    flag = False
                    break
            if flag:
                res += 1

print(res)