from time import process_time

text = input('введите текст: ')
mini, maxi = map(int, input('ввекдите диапозон от  и до  через пробел ').split())
otvet = text[mini - 1:maxi]
print(otvet)