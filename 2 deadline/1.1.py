num = int(input("введите положительное число: "))
yum = 0
while num > 0:
    yum += num % 10
    num //= 10
print("ответ: ", yum)
