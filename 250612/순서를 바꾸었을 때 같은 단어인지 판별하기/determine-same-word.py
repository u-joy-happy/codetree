word1 = input()
word2 = input()

# Please write your code here.

word1 = sorted(word1)
word2 = sorted(word2)

def is_same(word1, word2) :
    if len(word1) != len(word2) :
        return False

    for i in range(len(word1)) :
        if word1[i] != word2[i] :
            return False
    
    return True

print('Yes' if is_same(word1, word2) else 'No')