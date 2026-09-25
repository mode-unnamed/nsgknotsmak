import random
import string
def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string
message = input("Введите сообщение: ")
n = int(input("Введите количество подстановочных символов: "))
encoded = ""
for char in message:
    encoded += char + generate_random_string(n)
print("Закодированное послание:")
print(encoded)