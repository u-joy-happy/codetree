user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.

class User:
    def __init__(self, _id, level) :
        self._id = _id
        self.level = level

user1 = User('codetree', 10)
user2 = User(user2_id, user2_level)

print(f'user {user1._id} lv {user1.level}')
print(f'user {user2._id} lv {user2.level}')