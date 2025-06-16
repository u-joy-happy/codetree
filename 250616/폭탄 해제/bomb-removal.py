unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class DefusalManual:
    def __init__(self, unlock_code, wire_color, seconds) :
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

dm = DefusalManual(unlock_code, wire_color, seconds)

print(f'code : {dm.unlock_code}')
print(f'color : {dm.wire_color}')
print(f'second : {dm.seconds}')