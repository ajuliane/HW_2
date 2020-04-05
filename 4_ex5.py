from functools import reduce
def my_f(p1, p2):
    return p1 * p2

my_list=[el for el in range(100, 1001)]
print(reduce(my_f, my_list))
