
def get_minimum_length (*args):
    return len(sorted(args, key=len)[0])

def our_zip (*args):
    quantity = len(args)
    min_length = (get_minimum_length(*args))

    for i in range(0, min_length):
        mas = []
        count = 0
        for arg in args:
            count = count+1
            mas.append(arg[i])
            if count == quantity:
                tup = tuple(mas)
                print(tup)

x = 'python'
y = (10, 20, 30, 40)
z = 'ok'
e = (777, 666, 555)

print (list(zip(x,y,z, e)))
our_zip(x,y, z, e)




