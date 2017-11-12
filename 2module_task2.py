def my_function(a, param=[]):
    param.append(a)
    sum = 0
    for i in range(len(param)-1):
        sum += param[i]
    return sum


my_function(5)
print(my_function(3)) #return = 5
print(my_function(4)) # return = 8
print(my_function(6)) # return = 12
print (my_function (777)) #return = 18
#etc

