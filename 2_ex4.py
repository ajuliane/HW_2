a = input('Please write a sentence: ')
b = list()
b = a.split(' ')
for i, elem in enumerate(b):
    if len(elem)>10:
        print(i, elem[:11])
    else:
        print(i, elem)
