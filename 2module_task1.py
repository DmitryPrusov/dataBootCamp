import functools
def my_func (n):
    return functools.reduce(lambda x, y: x*y, range(1, n+1))














