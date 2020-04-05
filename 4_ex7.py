
def fact(n):
    result = 1
    for i in range(n):
        result=result*(i+1)
    return result
try:
    n = int(input('Enter the month as an integer: '))
except ValueError:
    print('Not a number entered!')

def generator():
    for el in range(n):
        yield fact(el+1)
g = generator()
for el in g:
    print(el)