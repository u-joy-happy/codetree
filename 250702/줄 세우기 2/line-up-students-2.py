n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.

class Student:
    def __init__(self, height, weight, idx):
        self.height, self.weight, self.idx = height, weight, idx

ss = [Student(students[i][0], students[i][1], students[i][2]) for i in range(n)]

ss.sort(key=lambda x : (x.height, -x.weight))

for s in ss :
    print(s.height, s.weight, s.idx)