class Dog():
    name = ""
    age = 0
    __breed = None
    def __init__(self, dog_name, dog_age, dog_breed):
        self.name = dog_name
        self.age = dog_age
        self.__breed = dog_breed
    def speak(self, sound):
        print(self.name, "says", sound)

    def run(self, speed):
        print(self.name, "runs", speed, "mph")

    def description(self):
        print(self.name, "is a", self.age,  "year old", self.__breed)

    def define_buddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

scout = Dog("Scout", 2, "Belgian Malinois")
print(scout)
#The output of print(scout) is <__main__.Dog object at 0x00000215DA58C3E0>
#This output is the default representation of the object in Python, 
#which includes the module name, the class name, and the memory address where the object is stored.

print(scout.name)
print(scout.age)
# print(scout.__breed)
# AttributeError: 'Dog' object has no attribute '__breed'
# The double underscore prefix means private attribute
# This prefix in Python makes the attribute a private member of the Dog class.
# It means that this attribute cannot be accessed directly from outside the class.
# In OOP terms, making __breed a private attribute and controlling access via methods follows the principle of encapsulation. 

scout.speak("woof")
scout.description()

skippy = Dog("Skippy", 3, "Border Collie")
scout.define_buddy(skippy)
scout.buddy.description() 


