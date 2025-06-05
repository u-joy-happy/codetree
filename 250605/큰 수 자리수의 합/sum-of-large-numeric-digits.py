a, b, c = map(int, input().split())

# Please write your code here.

def sum_number(n) :
    if n < 10 :
        return n
    return sum_number(n//10) + n % 10

print(sum_number(a*b*c)) 