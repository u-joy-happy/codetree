x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

min_x, min_y, max_x, max_y = 2000,2000,0,0
OFFSET = 1000

arr = [[0 for _ in range(2000+1)] for _ in range(2000+1)]

for i in range(2) :
    for y in range(y1[i], y2[i]) :
        for x in range(x1[i], x2[i]) :
            if i == 0 : arr[y+OFFSET][x+OFFSET] = 1
            elif i == 1 : arr[y+OFFSET][x+OFFSET] = 0
                
for y_axis in range(len(arr)) :
    for x_axis in range(len(arr[y_axis])) :
        if arr[y_axis][x_axis] == 0 :
            continue
        if x_axis <= min_x and y_axis <= min_y :
            min_x = x_axis
            min_y = y_axis
        if x_axis >= max_x and y_axis >= max_y :
            max_x = x_axis
            max_y = y_axis

print((max_x - min_x +1) * (max_y - min_y +1))
