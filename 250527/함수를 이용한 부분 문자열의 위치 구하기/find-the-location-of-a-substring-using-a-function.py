text = input()
pattern = input()

# Please write your code here.

def match_pattern():
    for i in range(len(text)) :
        if text[i:i+len(pattern)] == pattern :
            return i
    return -1

print(match_pattern())

