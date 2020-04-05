# First
from itertools import count
try:
    a = int(input('Enter the month as an integer: '))
    for el in count(a):
        if el > 9:
            break
        else:
            print(el)
except ValueError:
    print('Not a number entered!')

# Second
from itertools import cycle
c = 0
for i in cycle([1, 3, 5]):
    print(i)
    c += 1
    if c > 10:
        break