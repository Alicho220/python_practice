class Student:
    def __init__(self, first='', last='', id=0):
        self.first_name_str = first
        self.last_name_str = last
        self.id_int = id

    def update(self, first='', last='', id=0):
        if first:
            self.first_name_str = first
        if last:
            self.last_name_str = last
        if id:
            self.id_int = id

        # return"{} {}, ID:{}". format(self.first_name_str, self.last_name_str, self.id_int))

    def __str__(self):
        return "First Name is {} and the Last Name is {}, with ID:{}". format(self.first_name_str, self.last_name_str, self.id_int)

    __firstname = alicho

    


s1= Student(first='alicho', last = 'jimmy', id= 50)
s5 = Student("Nonso", "Godwin", 80)
print(s5)
print(s1)
s2 = Student(first='alicho', last = 'francis', id= 40)
s3 = Student(first='alicho', last = 'kelechi', id= 30)
s4 = Student(first='alicho', last = 'precious', id= 50)

s1.update(first='love', last='abass', id=20)
print(s4)

# Student.update(first='alicho', last = 'jimmy', id= 50)
# update = update()

# print(update)
