class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod #decorator
    def add_person(cls):
        cls.number_of_people += 1

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

p1 = Person("Bilal")
p2 = Person("Kerem")
print(Person.get_number_of_people())
print(p1.get_number_of_people())
