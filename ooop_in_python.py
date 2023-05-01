#oop
class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"hello, my name is {self.name} and i am {self.age} years old.")
person = person("hatim", 35)
person.say_hello()
print( person.name, person.age)
#the __str__() method
class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"person( name='{self.name}', age={self.age})"
person = person("hatim",35)
print(person)
#we can other inside function in class
class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduction(self):
        print("hello!! my name is", self.name)
person = person("hatim", 35)
person.introduction()
#self is instance parameter , can recall it with any name
class person: 
    def __init__(test, name, age):# first parameter inplace of test
        test.name = name
        test.age = age
    def introduction(abc): # seconde instance paramete inplace of self
        print("hello!! my name is", abc.name)
person = person("hatim", 35)
person.introduction()
#modify the properties of objects 
person.name = "maha"
person.age = 29
person.introduction()
#inheritance mechanisme
class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduction(self):
        print(f"hello, my name is {self.name} and i am {self.age} years old.")
class client(person):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address
    def introduction (self):
           print(f"hello dear client Ms{self.name}, you have {self.age} years old ago and you are living in {self.address}") 
client_1= client("hatim benjebara", 35, "8 avenue des FAR")
print(client_1.name)
print(client_1.age)
print(client_1.address)
client_1.introduction()
#input information
input_name = input("give me the name :")
input_age = int(input("give me the age: "))
input_address = input("give me the address :" )
clien_2 = client(input_name, input_age, input_address)
clien_2.introduction()
#we can create other class with 
class worker(person):
    pass
worker_1= worker("hatim", 35)
print(worker_1.name)
print(worker_1.age)
worker_1.introduction()
#in order to preserve the inheritance 
class worker(person):
    def __init__(self, name, age):
        person.__init__(self,name,age)
worker_1= worker("hatim", 35)
print(worker_1.name)
print(worker_1.age)

#super() function
class worker(person):
    def __init__(self, name, age):
        super().__init__(name, age)

