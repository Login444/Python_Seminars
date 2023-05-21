# 1  2  3  4  5  6  7   8   9  10  11
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

n = int(input('Введите n'))
a = 0
b = 1
i = 2

while b <= n:
    if b == n:
        print(i)
        break
    a, b = b, a + b
    i += 1
else:
    print(-1)