# test = [0, 1, 2, 3, 4, 5]
# print(test)

# test2 = [0] * 100
# print(test2)

# test3 = test + test2
# print(test3)

# test4 = list(range(90))
# print(test4)


test5 = list("Hello World I am Learning python and I am trying to covert this string to a list")

# print(test5)

# print(test4 + test5)



# index
# print(test5[1])

# to slice or to get a certain range of numbers
# print(test5[0:15])


# to loop ove an element in a list (it loops over 5 times)
# it can be used to get even numbers.
# using index of [::-1] make the number decrement where by counting from ascending to descending other
# print(test5[::5])


# uunpacking List : this means giving every element a variable.
unpack = list(range(20))
print(unpack)

# first, second, third, fourth, fifth, sixth, seventh, eight, nine, *rest, last  = unpack

# print(fifth, first, second, third)
# print(rest) # *rest has perfomed packing by the the * sign...
# print(last)





# looping through a loop
# for number in unpack:
#     print(number)


#enumerate turns the list to a set of immutable turples with key and values..
# for unmber in enumerate(unpack):
#     print(number)


# adding item
unpack.append("a",)
print(unpack)

#remove
unpack.remove(0)
print(unpack)

#removing the last letter, we use the pop function.
unpack.pop() # you can also pass an inde x
print(unpack)

# you can a delete a range of item
del unpack[0:5]


#removing all the item in a list...
unpack.clear()

#finding an index of a given object using the in operator
if 90 in unpack:
    print("its in")
    print(unpack.index(90))
else:
    print("not in the list")

print(unpack.count(1))

print(unpack.sort())

