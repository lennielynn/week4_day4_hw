
fib_cache = {}

def memoize(f):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = f(n)
            return cache[n]
        return wrapper





# @memoize
def fib_memo(n):
  if n <= 1:
    return 1
  if n not in fib_cache:
    fib_cache[n] = fib_memo(n - 1)  * n
  return fib_cache[n]

print(fib_memo(10))