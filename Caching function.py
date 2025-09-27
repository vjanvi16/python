
# Caching function :-

# 

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(4)
    return n*5

print(fx(4))
print("Done for 4")
print(fx(8))
print("Done for 8")
print(fx(16))
print("Done for 16\n")

print(fx(4))
print("Done for 4")
print(fx(8))
print("Done for 8")
print(fx(16))
print("Done for 16")