text = input("введите текст: ")
slovo = input("введите слово для поиска: ")
count = text.count(slovo)
if slovo in text:
    print(f"слово '{slovo}' найдено в тексте {count} раз")
else:
    print(f"cлово '{slovo}' не найдено в тексте")