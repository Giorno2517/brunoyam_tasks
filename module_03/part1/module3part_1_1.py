x = int(input('Вклад: '))
p = int(input('Годовой процент: '))
y = int(input('Желаемая сумма: '))
q = 0
clean = 0

yearly = x * (p / 100)
clean = y - x
q = clean / yearly

print('Вам понадобится', q, 'лет')
