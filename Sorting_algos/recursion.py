# Time: O(n)
# Space: O(1)
def frac(n):
    if n == 1:
        return 1
    return frac(n-1)*n

print(frac(4))


# Time: O(2^n)
# Space: O(1)
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)


# Time: O(n)
# Space: O(1)
def fib_mem(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    prev_list = fib_mem(n-1)
    s = prev_list[-1] + prev_list[-2]
    return prev_list + [s]

# Time: O(n)
# Space: O(1)
# ???
    

print(fib(7))
print(fib_mem(7))

