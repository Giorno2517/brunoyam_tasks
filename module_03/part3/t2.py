s = input('Текст: ')
k = int(input('Количество: '))

for i in s.split():
    if len(i) < k:
        print(i)
