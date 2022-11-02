class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print("Name is :", self.name, " and age is: ", self.age)


class Student(Person):
    def __init__(self, name, age, marks):
        Person.__init__(self,name,age)
        self.marks = marks

    def print(self):
        print("Name is :", self.name, " and age is: ", self.age, " and marks is: ", self.marks)

s1=Student("tushar", 23, 30)
s1.print()
