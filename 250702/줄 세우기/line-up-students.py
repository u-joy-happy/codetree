from functools import cmp_to_key

n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.

def compare(s1, s2) :
    if s1[0] > s2[0] :
        return -1
    elif s1[0] == s2[0] and s1[1] > s2[1] :
        return -1
    elif s1[0] == s2[0] and s1[1] == s2[1] and s1[2] < s2[2] :
        return -1
    return 1

students.sort(key=cmp_to_key(compare))

for st in students :
    print(st[0], st[1], st[2])
