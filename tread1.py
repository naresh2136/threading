import time


def test1(x, y):
    for i in range(x, y):
        print(i)
        time.sleep(2)


def test2(a, b):
    for j in range(a, b):
        print(j)
        time.sleep(1)


test1(2, 5)
print("-----------------")
test2(6, 10)
