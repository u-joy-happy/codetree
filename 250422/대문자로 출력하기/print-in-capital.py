n = input()

for item in n :
    if item.isalpha() :
        if item >= 'A' and item <= 'Z':
            print(item, end='')
        else :
            code = ord('A') + (ord(item) - ord('a'))
            print(chr(code), end='')