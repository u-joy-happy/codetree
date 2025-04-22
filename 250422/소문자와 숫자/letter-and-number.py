n = input()

for item in n :
    if item >= 'a' and item <= 'z' :
        print(item, end='')
    elif item >= 'A' and item <= 'Z' :
        code = ord('a') + (ord(item) - ord('A'))
        item = chr(code)
        print(item, end='')
    elif item >= '0' and item <= '9' :
        print(item, end='')
