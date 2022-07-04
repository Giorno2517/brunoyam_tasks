import json

#data = {'testlog1': 'testpasswd1'}
#with open('register.json', 'w') as f:
#    json.dump(data, f)

login = input('Введите логин: ')
passwd = input('Введите пароль: ')


def register(login, passwd):
    with open('register.json', 'r') as f:
        data = json.load(f)
    if login in data.keys():
        print('Логин занят')
    else:
        data[login] = passwd
        with open('register.json', 'w') as f:
            json.dump(data, f)
        print('Регистрация успешна!')


register(login, passwd)
