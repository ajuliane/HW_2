my_list = [7, 5, 3, 3, 2]
a = int(input('Put new value of rating: '))

for i in range(len(my_list)):
    if (i < len(my_list)-1) and (my_list[i+1] < a):
        my_list.insert(i+1, a)
        break
    #elif my_list[i+1] >= a:
    if i >= len(my_list)-1:
        my_list.append(a)

print(my_list)