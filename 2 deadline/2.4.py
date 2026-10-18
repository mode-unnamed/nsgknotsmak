n = int(input('введите высоту: '))
a = 1
while a <= 1:
    line = " " * (n - a)
    b = 1
    while b <= a:
        line += str(b)
        b += 1
    b = a - 1
    while b >= 1:
        line += str(b)
        b -= 1
print(line)