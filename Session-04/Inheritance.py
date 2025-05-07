class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)
        
x = Person("Naman", "Karki")
x.printname()

class Student(Person):
    pass

y=Student("Karan", "Palriwal")
y.printname()

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.


#Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is an animal.")
    
    def speak(self):
        print(f"{self.name} makes a sound")
        
#Child Class
class Dog(Animal):
    def __init__(self, name,breed):
        #Call the parent class constructor
        super().__init__(name)
        self.breed=breed
        print(f"{self.name} is a {self.breed} dog.")
    def speak(self):
        super().speak()
        print(f"{self.name} barks")
        
my_dog = Dog("Wishky", "Coocker Spaniel")
my_dog.speak()