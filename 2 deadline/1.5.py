text = input("введите предложение: ")
bykva = "уеыаоэюяё"
result = ""
i = 0
while i < len(text):
    if text[i].lower() not in bykva:
        result += text[i]
    i += 1
print('результат ', result)