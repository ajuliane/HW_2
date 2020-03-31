
# List
try:
    a = int(input('Enter the month as an integer: '))
    if a in [12, 1, 2]:
        print('winter')
    elif a in [3, 4, 5]:
        print('spring')
    elif a in [6, 7, 8]:
        print('summer')
    elif a in [9, 10, 11]:
        print('autumn')
    else:
        print('It is not right number')
except ValueError:
    print('Not a number entered!')

# Dict
b = {'1': 'winter', '2': 'winter', '12': 'winter'}
c = {'3': 'spring', '4': 'spring', '5': 'spring'}
d = {'6': 'summer', '7': 'summer', '8': 'summer'}
e = {'9': 'autumn', '10': 'autumn', '11': 'autumn'}
try:
    a = int(input('Enter the month as an integer: '))
    if a in b.keys():
        print('winter')
    elif a in c.keys():
        print('spring')
    elif a in d.keys():
        print('summer')
    elif a in e.keys():
        print('autumn')
    else:
        print('It is not right number')
except ValueError:
    print('Not a number entered!')