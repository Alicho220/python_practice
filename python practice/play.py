my_list = []
sentinel = -1

num = int(input('enter number: '))
while num != sentinel:
    my_list.append(num)
    print(my_list)
    num = int(input('enter number: '))


print("Thank you")

my_list.sort()

print(my_list)
