y = int(input())

# Please write your code here.

def is_leap(y) :
    if y % 100 == 0 and y % 400 != 0 :
        return False 
    if y % 4 == 0 :
        return True 
    return False

if is_leap(y) :
    print('true')
else :
    print('false')
