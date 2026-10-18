from sys import prefix

text = input("введите предложение: ")
lefo, pravo = 0, len(text) - 1
otvet = True
while lefo < pravo:
    if text[lefo] != text[pravo]:
        otvet = False
        break
    lefo += 1
    pravo -= 1
print("это палидрон" if otvet else "это не вот это")