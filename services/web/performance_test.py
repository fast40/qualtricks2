from time import time, sleep
from random import randint


def timeit(func, *args, **kwargs):
    t = time()

    func(*args, **kwargs)

    print(time() - t)


x1 = [randint(0, 256) for _ in range(10000)]
x2 = [randint(0, 256) for _ in range(10000)]

def remove(x1, x2):
    return [i for i in x1 if i not in x2]

def remove2(x1, x2):
    f = [i for i in filter(lambda i: i not in x2, x1)]
    print(f)
    return f


print(timeit(remove, x1, x2))
print(timeit(remove2, x1, x2))