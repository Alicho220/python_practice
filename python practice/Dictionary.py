# key value pair eg a phone book..
# name to a contact detail where name is the key and the cd is the value
# use string for the key and anytype for the value
# you can get the value associtaed with a key using index.. which is a name of a key.

point = {"x":1, "y":2}
point = dict(x=1,y=2)
print (point)

# to get an index use the get function..

x = point.get("x")
print(x)

#  you can also delete an element

del point["x"]

# loop

for key in point:
    print(key, point[key])