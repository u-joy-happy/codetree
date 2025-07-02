from functools import cmp_to_key

n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.

class Note :
    def __init__(self, idx, x, y) :
        self.idx, self.x, self.y = idx, x, y

notes = [Note(points[i][0]+1, points[i][1][0], points[i][1][1]) for i in range(n)]

def compare(n1, n2) :
    if abs(n1.x) + abs(n1.y) > abs(n2.x) + abs(n2.y) :
        return 1
    elif abs(n1.x) + abs(n1.y) == abs(n2.x) + abs(n2.y) and n1.idx > n2.idx :
        return 1
    return -1

notes.sort(key=cmp_to_key(compare))

for n in notes:
    print(n.idx)
