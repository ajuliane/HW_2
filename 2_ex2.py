a = input('Enter the list items. If you want stop process then enter 0: ')
b = list()

j = 0
while a!= '0':
    b.append(a)
    a = input('Enter the list items. If you want stop process then enter 0: ')
    #if a=='0':
       # break
if a == '0':
   # print (b)
    for i in range(int(len(b)/2)):
        b[j], b[j+1] = b[j+1], b[j]
        j = j+2


print(b)