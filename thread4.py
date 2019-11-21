import threading
import time


def test1(x, y):
    for i in range(x, y):
        print(threading.currentThread().getName(), i)
        time.sleep(2)


def test2(a, b):
    for j in range(a, b):
        print(threading.currentThread().getName(), j)
        time.sleep(1)


t1 = threading.Thread(target=test1, args=(2, 5))
t2 = threading.Thread(target=test2, args=(7, 11))

t1.setName("tx1")
t2.setName("tx2")

t1.start()
t2.start()

t1.join()
t2.join()

print("This is main program..")
