a = int(input('введите сторону a = '))
b = int(input('введите сторону b = '))
c = int(input('введите сторону c = '))
s = 0


def area(a, b, c):
    global s
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5


area(a, b, c)
print('Площадь = ', s)
