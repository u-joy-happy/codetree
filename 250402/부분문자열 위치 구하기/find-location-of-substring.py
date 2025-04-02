input_str = input()
target_str = input()

# Please write your code here.

idx = -1

for i in range(len(input_str) - len(target_str)):
    div_str = input_str[i:i+len(target_str)]
    if div_str == target_str :
        idx = i

print(idx)