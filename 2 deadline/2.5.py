a = int(input('сколько чисел?: '))
num = []
x = 1
while x <=a:
    num.append(float(input('введите число ' + str(x) + ': ')))
    x += 1
average = sum(num) / len(num)
print('РЕЗУЛЬТАТЫ: ')
print('максимальное: ', max(num))
print('минимальное: ', min(num))
print('среднее: ', average)
print('чисел больше среднего: ', len([x for x in num if x > average]))