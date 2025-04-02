A = input()

# Please write your code here.

# cnt_arr = [0 for _ in range(ord('z') - ord('a') + 1)]
str_arr = []
cnt_arr = []

str_arr.append(A[0])
cnt_arr.append(1)

if len(A) > 1 :
    for i in range(1, len(A)):
        if str_arr[-1] != A[i] :
            str_arr.append(A[i])
            cnt_arr.append(1)
        else :
            cnt_arr[-1] += 1

res = ''
for i in range(len(str_arr)):
    res += str_arr[i] + str(cnt_arr[i])

print(len(res))
print(res)
