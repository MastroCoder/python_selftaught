class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def obj_equal(a, b):
    if a is b:
        return True
    else:
        return False

Mike = Person("Mike", 50)
#Yike = Person("Yike", 45)
Yike = Mike

if(obj_equal(Mike, Yike)):
    print("Equal! Horray! You are the same!")
else:
    print("Unequal!")
