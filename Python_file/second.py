def gen_func():
    sum=0
    for i in range(1,10):
        sum+=i
        yield sum
if __name__=="__main__":
    result=gen_func()
    print(result.__next__())
    print("after start the execution for end value")
    for j in result:
        print(f"this iterate number wise:-{j}")

def add_decorator(func):
    def wrapper(a,b,*args,**kwargs):
        # result=a+b
        # print(result)
        result=func(a,b)
        return result
    return wrapper
@add_decorator
def add(a,b):
    add_value=a+b
    return add_value
result=add(10,20)
print(result)

ls1=[1,2,3,4,[10,20,30]]
ls2=ls1.copy()
print(id(ls1[4]))
print(id(ls2[4]))
ls2[4][0]=11111
print(ls2)
print(ls1)

config = {"settings": {"theme": "dark", "version": 1.0}}
temp_config=config.copy()
temp_config["settings"]["version"]=2.0
print(temp_config)
print(config)

import threading
import time
import requests

def fetch_url(url):
    response=requests.get(url)
    print(f"Fetched {url}: {len(response.text)} characters")

urls={

    "https://www.example.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
}
threads=[threading.Thread(target=fetch_url(url,)) for url in urls]
if __name__=="__main__":
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function

if __name__=="__main__":
    result=outer_function(10)
    print(result(7))

def multiple(factor):
    def factor_func(x):
        result=factor ** x
        return result
    return factor_func

result=multiple(5)
print(result(3))

is_even=lambda x:x%2==0
for i in range(1,10):
    if is_even(i)%2==0:
        print("even")
    else:
        print("odd")

number=[1,2,3,4,5,6,7,8]
def func(n):
    if n%2==0:
        return "Even Number"

if __name__=="__main__":
    result=map(func,number)
    print(next(result))
    print("After next value execuation start")
    print(next(result))

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def method1(self):
        return f"My name is {self.name}-{self.age}"
    
    def method2(self):
        return self.method1()

obj1=Person("Shri",20)
print(obj1.method1())

class MyOtherPerson(type):
    def __new__(cls,name,bases,dct):
        dct["name"]=lambda self: f"Hello from {name}!"
        return super().__new__(cls,bases,name,dct)

class MyPerson(metaclass=MyOtherPerson):
    pass

obj1=MyPerson()
print(obj1.name())

class UpperCaseClass(type):
    def __new__(cls,bases,name,dct):
        uppercase={
           i.upper():v for i,v in dct.items() if not i.startswith('__')

       }
        return super().__new__(cls,bases,name,uppercase)
    
class Myclass(metaclass=UpperCaseClass):

    attribute="hello"
    
obj1=Myclass()
print(hasattr(Myclass, "ATTRIBUTE"))

class MyDetail(object):
    def __new__(cls,*args,**kwargs):
        print("this is new instance is created")
        instance=super().__new__(cls)
        return instance
    
    def __init__(self,value):
        self.value=200

obj1=MyDetail("hello")
print(obj1.value)

def func(a, b, c, d):
    return (a, b, c, d)

arg_value = (1, 2)
kwarg_value = {"name": "shri", "age": 23}  # Use curly braces for a dictionary

print(func(*arg_value, **kwarg_value))

class Animal:
    def __init__(self,species):
        self.species=species

    def make_sound(self):
        print("Some gerneric animal sound")

class Dog(Animal):
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def make_sound(self):
        super().make_sound()
        print("Woof")

obj1=Dog("jacky","Golden")
print(obj1.make_sound())

def add_decorator(func):
    def wrapper(a,b,*args,**kwargs):
        # result=a+b
        result1=func(a,b)
        print(result1)
    return wrapper

@add_decorator
def say_hello(a,b):
    return a+b
result=say_hello(10,20)
result

class Person:
    location="indore"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def method1(self):
        return f"this is method 1 to fetch the instance attribute {self.name}-{self.age}"

    @classmethod
    def method2(cls):
        return f"this is only access in class variable:-{cls.location}"
    
    @staticmethod
    def method3(input):
        sum=0
        for i in range(input):
            sum+=i
        return f"Total value in {sum}"
    
    @property
    def method4(self,user1):
        self.user1=user1
        return f"this is method with using property method {self.user1}"
    
obj1=Person("shri",25)
print(obj1.method1())
print(obj1.method2())
print(obj1.method3(10))
        
def generator_func(input):
    sum=0
    for i in range(0,input):
        sum+=i
        yield sum

if __name__=="__main__":
    result=generator_func(10)
    print(next(result))
    print("after start the iteration in remaining value")
    for k in result:
        print(f"Iteration value",k)

ls1=[10,20,30,40,[1,2,3,4]]
ls2=ls1.copy()
print(id(ls1[4]))
print(id(ls2[4]))

ls2[4][0]=10000
print(f"this is copy object{ls2}")
print(f"this is original object{ls1}")

class Car(object):
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def method1(self,colour):
        self.colour=colour 
        return f"this is return value for this car:-{self.make}-{self.model}-{self.colour}"

obj1=Car("Mahindra","Bolero")
print(obj1.method1("White"))

class Payment(object):
    def __init__(self,amount,transaction_id,date):
        self.amount=amount
        self.__transaction_id=transaction_id
        self.date=date

    def __method1(self):
        return f"this is private attribute for tranaction{self.__transaction_id}"
    
obj1=Payment(100000000,"erueru9r80-8989d-898fdfjdfh","2024-12-05")
print(obj1.__method1())

class Shape(object):
    def area(self):
        pass

class Recatangle(Shape):
    def area(self):
        return f"this is overriding this inheritance class"
    
obj1=Recatangle()
print(obj1.area())

class GrandParent(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Parent(GrandParent):
    def __init__(self,name,age,parent_name):
        super().__init__(name,age)
        self.__parent_name=parent_name

    def method1(self):
        return f"this is detail for Parent and Gransparet object:-{self.__parent_name}-{self.name}-{self.age}"
    
par_obj=Parent("parent_test","grand_test",24)
print(par_obj.method1())

class Employee(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class Salary(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.gender=gender
        self.age=age

    def jump(self):
        return f"this is jump method called"
    
class Male(Employee,Salary):
    def __init__(self,name,age,gender,location):
        super().__init__(name,age,gender)
        super().__init__(name,age,gender)
        self.location=location

    def method1(self):
        return f"this is value:{self.name}-{self.age}-{self.location}-{self.gender}"
    
    def method2(self):
        return f"this is called for Salary method with {super().jump()}"

obj1=Male("test_name","23","male","indore")
print(obj1.method1())
print(obj1.method2())  

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"Initialized Person: {self.name}, {self.age} years old")

class Employee(Person):
    def __init__(self,name,age,employee_id,department):
        super().__init__(name,age)
        self.employee_id=employee_id
        self.department=department
        print(f"Initialized Employee: ID={self.employee_id}, Department={self.department}")

class Manager(Employee):
    def __init__(self,name,age,employee_id,department,team):
        super().__init__(name,age,employee_id,department)
        self.team=team
        print(f"Initialized Manager: Team={', '.join(self.team)}")

manager=Manager("test_user",23,"13829382","Developer",team=["Bob", "Charlie", "Diana"])
print(manager)