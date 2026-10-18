yum = 0
num = int(input("введите любое число кроме 0: "))
while num != 0:
    yum += 1
    num = int(input("еще "))
print("кол-во чисел = ", yum)
