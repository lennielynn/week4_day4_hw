def count_calls(f):
    def wrapper_count(*args):
        wrapper_count.call_count += 1
        return f(*args)
    
    wrapper_count.call_count = 0
    return wrapper_count


cache = {}

@count_calls
def fib_memo(num):
    if num <= 1:
        return 1
    if num not in cache:
        cache[num] = fib_memo(num - 1) * num
    return cache[num]


for r in range(1, 11):
    test_result = fib_memo(r)
    print(f"fib({r}) = {test_result}, Function Calls = {fib_memo.call_count}")