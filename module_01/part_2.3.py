Password = str(input('Введите пароль: '))
while len(Password) <= 8 or Password.islower() or Password.isupper():
    print('Пароль должен состовлять не менее 8 букв верхнего и нижнего регистра')
    Password = str(input('Введите пароль: '))
else:
    print('Пароль принят')