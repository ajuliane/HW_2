# First
#def my_func(x,y):
#    result=x**y
#    print (result)
# Second
def my_func(x, y):

    if y > 0:
        result = 1
        for i in range(y):
            result = x * result
        print(result)
    elif y == 0:
        print(x)
    elif y < 0:
        result2 = 1
        for i in range(abs(y)):
            result2 = result2/ x
        print(result2)

my_func(2, 4)
my_func(2, -4)
my_func(2, 0)


