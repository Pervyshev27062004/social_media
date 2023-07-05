class Person:

    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"{self.name} is {self.age}")


Alex = Person("alex")
Alex.age = 20
Alex.display_info()
