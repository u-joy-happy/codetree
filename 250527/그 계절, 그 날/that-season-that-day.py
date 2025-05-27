Y, M, D = map(int, input().split())

# Please write your code here.

def is_valid_date(Y, M, D) :

    if M <= 7 :
        if M % 2 == 1 :
            if D <= 31 : return True
            else : return False
        elif M != 2 :
            if D <= 30 : return True
            else : return False
        else :
            if is_leaf_year(Y) and D <= 29 : return True
            elif D <= 28 : return True
            else : return False

    elif M >= 8 and M <= 12 :
        if M % 2 == 0 :
            if D <= 31 : return True
            else : return False
        else :
            if D <= 30 : return True
            else : return False
    
    return False


def is_leaf_year(Y) :
    if Y % 4 == 0 :
        if Y % 100 == 0 and Y % 400 == 0 :
            return True  
        if Y % 100 == 0 :
            return False
        return True
    return False


def get_season(M) :
    if M >= 3 and M <= 5 :
        return('Spring')
    elif M >= 6 and M <= 8 :
        return('Summer')
    elif M >= 9 and M <= 11 :
        return('Fall')
    elif M <= 2 or M == 12 :
        return('Winter')


if is_valid_date(Y, M, D) :
    print(get_season(M))
else :
    print(-1)