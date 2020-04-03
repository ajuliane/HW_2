def int_func(x):
    try:
        print(x.title())
    except AttributeError:
        print('Not a string entered!')
#int_func(4)
#int_func('text')
a = input('Please enter words separated by space: ').split()

result = list((map(int_func, a)))
print(result)

