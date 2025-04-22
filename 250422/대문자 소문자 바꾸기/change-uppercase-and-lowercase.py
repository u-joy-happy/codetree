n = input()

for item in n :
    if item >= 'A' and item <= 'Z' :
        code = ord('a') + (ord(item) - ord('A'))
    elif item >= 'a' and item <= 'z' :
        code = ord('A') + (ord(item) - ord('a'))
    print(chr(code), end='')