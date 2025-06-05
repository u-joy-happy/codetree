N = int(input())

# Please write your code here.

def sum_number(n) :
    if n == 1 or n == 2:
        return n
    return sum_number(n - 2) + n


print(sum_number(N))