# CLASSES NOTES

# TO DO LIST
# make a person class
# create an instance of Person class
# give the object attributes
# change the attributes using dot notation
# use a constructor to assign attributes

class Person():
    feet = True
    face = True
    age = 0
    name = "Doe"
    apples = 2

    def __init__(self, name):
        self.name = name
        print("a new person named", self.name, "has been added")

    def say_hi(self):
        print(self.name, "says hi")

class Student(Person):
    def give_apple(self, teacher):
        if self.apples > 0:
            self.apples -= 1
            teacher.apples += 1
            print(self.name, "gives an apple to", teacher.name)

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.apples = 0
        print("a new teacher has been added")

    def eat_apple(self):
        if self.apples > 0:
            print(self.name, "ate an apple")
            self.apples -= 1


person1 = Person("Ava")
person1.age = 10
# print(person1.age)
person1.x = 100
# print(person1.x)
person1.say_hi()

person2 = Student("Bob")
person2.say_hi()

person3 = Teacher("Cal")

person2.give_apple(person3)

benji = Student("Benji")
