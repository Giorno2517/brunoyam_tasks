a = int(input())
b = int(input())
c = int(input())

if a == b:
    if a == c:
        print(3)
    else:
        print(2)
else:
    if b == c:
        print(2)
    else:
        if c == a:
            print(2)
        else:
            print(0)