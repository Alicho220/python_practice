# collection with no duplicate..
# if you have a list and want no duplicate of element just convert to a set
# we cannot index a set 

numbers = [1,1,1, 2,2,2,4,5,6,7,6]

numbers1 = set(numbers)
numbers2 = {1,4,10,50}
print(numbers1)
# you can add, remove
# numbers1.add()
# numbers1.remove()
# len(numbers1)

# union of two set
union = numbers1 | numbers2
print(union)

intersection = numbers1 & numbers2
print(intersection)

print(numbers2 - numbers1)