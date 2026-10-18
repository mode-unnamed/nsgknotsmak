text = input("введите текст: ")
shag = int(input("введите шаг: "))
result = text[::shag]
print("текст с шагом:", result)