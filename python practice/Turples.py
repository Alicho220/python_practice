# use it to in a position  where you dont want to accidentally edit elements..

# read only list that can not be modified ()

point =(1, 2, 4)
point2 = 1, 2
point3 =()


# you can concartinmate two turples
# * is used to replicate the turple
point4 = point + point2
print(point4)


point5 = point * 3
print(point5)


# list can be converted to a turple using a turple function..
list1=tuple([1,2])
list2= tuple("Hello world")
print(list2)
print(list1)



# you can find the range of element in a turple
point = point[0:2]
print(point)

if 2 in point:
    print("Exist")

