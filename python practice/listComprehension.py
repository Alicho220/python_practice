#list comprehension and map are the same thing....

(values ) = [(expresiion) for (value) in (collection)]

items =[
    ("product", 10),
    ("product", 9),
    ("product", 90)

]

prices = [item[1] for item in items]
print(prices)