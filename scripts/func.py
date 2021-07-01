from functools import lru_cache


@lru_cache(maxsize=32)
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


for i,v in enumerate(fib()):
    print("{}:{}".format(i,v))
    if i > 100:
        break

