X, Y = map(int, input().split())

# Please write your code here.

def inter_num(n):
    num_str = str(n)
    for i in range(len(num_str)):
        cnt = 0
        for j in range(len(num_str)):
            if num_str[i] == num_str[j] :
                cnt += 1
        if cnt == len(num_str) - 1 :
            return True
    return False
    

res = 0
for num in range(X, Y+1):
    if inter_num(num):
        res += 1

print(res)