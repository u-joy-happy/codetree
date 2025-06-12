secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class Mission:
    def __init__(self, code, loc, time):
        self.code = code
        self.loc = loc
        self.time = time

m = Mission(secret_code, meeting_point, time)
print(f'secret code : {m.code}')
print(f'meeting point : {m.loc}')
print(f'time : {m.time}')