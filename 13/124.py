points_num = int(input('How many points are you gonna create? '))

points = []
for i in range(points_num):
    pair = []
    x = float(input('Enter x: '))
    y = float(input('Enter y: '))
    points.append([x, y])
sumx = 0
sumy = 0
sumxy = 0
sumx_square = 0
for pair in points:
    sumx = sumx + pair[0]
    sumy = sumy + pair[1]
    sumxy = sumxy + pair[0] * pair[1]
    sumx_square = sumx_square + pair[0] ** 2


n = points_num
m = (((sumxy - (sumx * sumy)) / (n)) / ((sumx_square - (sumx ** 2)) / (n)))

meanx = sumx / n
meany = sumy / n

b = meany - meanx * m

m = round(m, 2)
b = round(b, 2)

print(f'y = {n}x + {b}')