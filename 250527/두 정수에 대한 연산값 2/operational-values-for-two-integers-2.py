a, b = map(int, input().split())

# Please write your code here.

def calcul_int(a, b):
    if a < b :
        return a + 10, b * 2
    else :
        return a * 2, b + 10

a, b = calcul_int(a, b)

print(a, b)