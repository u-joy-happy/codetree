n = int(input())

# Please write your code here.

def div_num(n):
    sum_val = 0
    for i in range(n):
        sum_val += (i + 1)

    return sum_val // 10

print(div_num(n)) 