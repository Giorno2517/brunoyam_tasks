import json

data = {'testlog1': 'testpasswd1'}
secret_info = 57
with open('register.json', 'r') as f:
    data = json.load(f)

login = input('Введите логин: ')
passwd = input('Введите пароль: ')


def login_function(login, passwd):
    if login in data.keys():
        if data[login] == passwd:
            print('Успешный вход!')
            print(secret_info)
        else:
            print('Неверный пароль')
    else:
        print('Неверный логин')


login_function(login, passwd)
