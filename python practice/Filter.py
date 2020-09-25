# filters item out of a sequence..
# returns filtered list..

items =[
    ("product", 10),
    ("product", 9),
    ("product", 90)

]

filtered = list(filter(lambda item:item[1] >=10, items))
print(filtered)