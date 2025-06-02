N = int(input())

# Please write your code here.

def fact_add(n) :
    if n == 1 :
        return 1
    return fact_add(n-1) + n


print(fact_add(N))