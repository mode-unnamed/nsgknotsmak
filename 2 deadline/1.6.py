symbol = input('введите число: ')
visota = input('введите высоту: ')
shirina = input('введите ширину: ')
a = 0
while a < visota:
    line = ''
    col = 0
    while col < shirina:
        line += symbol
        col += 1
    print(line)
    a += 1