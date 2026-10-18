text = input('введите текст: ')
byk = chis = znak = space = 0
marks = '.,!;:?'
a = 0
while a < len(text):
    yt = text[a]
    if yt.isalpha():
        byk +=1
    elif yt.isdigit():
        chis += 1
    elif yt in marks:
        znak += 1
    elif yt ==" ":
        space += 1
    a += 1
print('букв = ', byk)
print('цифр = ', chis)
print('знаков препин. = ', znak)
print('пробелов = ', space)