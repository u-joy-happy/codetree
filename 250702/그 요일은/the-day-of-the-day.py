m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

date1, date2 = 0, 0

for i in range(1, 13):
    if i < m1 : date1 += months[i]
    if i < m2 : date2 += months[i]

date1 += d1
date2 += d2

date_diff = date2 - date1 + 2
dow_diff = dow.index(A)

print(date_diff//7)