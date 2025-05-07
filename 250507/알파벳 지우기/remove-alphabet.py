a = input()
b = input()

new_str1 = ''
new_str2 = ''

for item in a :
    if item.isdigit() :
        new_str1 += item

for item in b :
    if item.isdigit() :
        new_str2 += item

print(int(new_str1) + int(new_str2))