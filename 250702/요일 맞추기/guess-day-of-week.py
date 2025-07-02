m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

date1, date2 = 0, 0

for i in range(13):
    if i < m1 :
        date1 += months[i]
    if i < m2 :
        date2 += months[i]
date1 += d1
date2 += d2

diff = date2 - date1 

print(dow[diff % 7])