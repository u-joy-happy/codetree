N = int(input())

# Please write your code here.

cnt_val = 0

def div_num(n):
    global cnt_val

    if n == 1 :
        return 
    cnt_val += 1
    
    if n % 2 == 0 :
        return div_num(n//2)
    else :
        return div_num(n//3)


div_num(N)
print(cnt_val)