def my_func(arg1, arg2, arg3):
    a=sorted([arg1, arg2, arg3])
    result = 0
    for index, number in enumerate(a[:2]):
        result = result + number
    print (result)

my_func(1,9,3)


