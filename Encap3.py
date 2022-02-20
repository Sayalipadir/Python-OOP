class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age

    def display(self):
        print(self.name)
        print(self._age)


person = Person('Snehal', 20)
# accessing using class method
person.display()
# accessing directly from outside
print(person.name)
print(person._age)