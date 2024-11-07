import functools
import time

@functools.lru_cache(maxsize=None)
def square(n):
    if n < 0:
        return n
    time.sleep(3)
    return n**2


print(square(10))
print(square(20))
print(square(5))


print(square(10))
print(square(20))
print(square(5))
print(square(9))