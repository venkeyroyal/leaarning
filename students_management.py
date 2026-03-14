class Person:

    def __init__(self,name):     # constructor
        self.name = name


class Student(Person):          # inheritance

    def __init__(self,name,marks):
        super().__init__(name)
        self.__marks = marks    # encapsulation

    def show(self):
        print("Name:",self.name)
        print("Marks:",self.__marks)


s = Student("Venky",90)
s.show()