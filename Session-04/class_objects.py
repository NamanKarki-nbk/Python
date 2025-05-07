class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
p1 = Person("Jhon", 45)

print(p1.name)
print(p1.age)

#str() fucntions control what should be returned when the class cobject is represented as a string

class Dota:
    def __init__(self, name , role):
        self.name= name
        self.role=role
    def __str__(self):
        return f"{self.name}({self.role})"

p1 = Dota("Pudge", "Hook")
print(p1)
        