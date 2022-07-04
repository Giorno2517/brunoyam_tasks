a = int(input())
q = 0

while a != 0:
    q = (a % 10) + q
    a = a // 10

print(q)