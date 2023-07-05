class Person:

    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"{self.name} is {self.age}")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying")


Alex = Student("Alex")
Alex.age = 20
Alex.display_info()
Alex.study()


class Phone:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def display_attribute(self):
        print(f"{self.name} has color {self.color} and model {self.model}")


Iphone = Phone("IPhone", "black", 14)
Iphone.display_attribute()
