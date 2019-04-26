from random import randint

x = randint(0, 9)
y = randint(0, 9)
print(x)
print(y)


if x > y:
    print(True)
else:
    print(False)

if x*2 > y:
    print(True)
else:
    print(False)

if y < (x + 3) and y > (x - 2):
    print(True)
else:
    print(False)

if (x * y) % 2 == 0:
    print(True)
else:
    print(False)
