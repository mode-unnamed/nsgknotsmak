passw = input('введите пароль: ')
twopassw = input('подтвердите пароль: ')
if passw == twopassw:
    login = input('введите паролья для входа')
    if login == passw:
        print('успешно')
    else:
        print('неуспешно')
else:
    print('пароли разные')
    