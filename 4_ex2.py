my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new=list()

for id, item in enumerate(my_list):
   if int(id) == 0:
       continue
   if int(my_list[id] )>int(my_list[id-1]):
       new.append(my_list[id])
print(new)
