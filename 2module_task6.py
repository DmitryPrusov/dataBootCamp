def otladka_results(func):
    def wrapper(*func_args, **func_kwargs):
        retval = func(*func_args,**func_kwargs)
        print('name of the function: ' + func.__name__)
        print ('parameters values: ')
        for arg in func_args: print(arg, end=',')
        print('\nreturns ' + repr(retval))
        return retval
    wrapper.__name__ = func.__name__
    return wrapper

@otladka_results
def my_suma(*args):
    sum = 0
    for arg in args:
        sum+=arg
    return sum

my_suma(4, 5, 7, 3)

