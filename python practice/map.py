# apply same function to each element of a sequence
# return the modified list

mylist = list(range(10))


mylist =list(map(lambda x: x**2, mylist))
print(mylist)