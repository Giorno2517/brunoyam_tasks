a = [1, 4, 5, 1, 'hello', 5, 10, 8, 'hello']
b = []

for i in a:
    if a.count(i) > 1 and b.count(i) == 0:
        b.append(i)

print(b)