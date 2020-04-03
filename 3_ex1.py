def my_func(arg1, arg2):
    print(f'{(arg1/arg2):.2f}')

try:
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))
    my_func(a, b)
#except ValueError:
    #print('Not a number entered!')
except TypeError:
    print('Not a number entered!')
except ZeroDivisionError:
    print('You cannot divide by zero!')