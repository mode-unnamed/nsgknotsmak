from random import randint
zagad = randint(1, 100)
nachal = int(input('угадайте число от 1 до 100: '))
while nachal != zagad:
    if nachal < zagad:
        print("больше")
    else:
        print("меньше")
print("угадал")