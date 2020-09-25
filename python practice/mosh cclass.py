# for number in range(5):
#     print(number)
#     print("Attempt", number + 1, (number +1) * ".")
    
#     print((number + 1)* "*")


#for else loop..
# attempt=True
# for number in range(3):
#     print("Attempt")
#     if attempt:
#         print("Grant Access")
#         break 
# else:
#     print("More than 3 trial")


#nested for loop where the second for loop is the child of the first..  
#it works in a form where the first is the row and the second a column
# for x in range(5):
#     for y in range(4):
#         print(f"( {x},{y})")

my_list = []
command=""
while command.lower() !="quit":
    command=input("Enter Item bought: ")
    print("Item", command)
    