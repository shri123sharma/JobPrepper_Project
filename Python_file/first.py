def generate_func():
    sum_val=0
    for i in range(1,10):
        sum_val+=i
        yield sum_val

result=generate_func()
print(next(result))

def decorator_func(func):
    def inner_func(*args,**kwargs):
        x,y=args[1],args[0]
        result=func(x,y)
        return result
    return inner_func
@decorator_func
def say_hello(x,y):
    return x,y
print(say_hello(10,20))

ls1=[1,2,3,4,5]
ts1=(1,2,3,4,5)
ss1={10,20,30,40,50}
ds1={'a':100,"b":200,"c":300}
for i in ls1:
    print(i)
print(dir(ls1))
print(type(ls1))

ls2=iter(ls1)
for j in ls2:
    print(f"iterator:-{j}")

import threading
import time

def func1():
    for i in range(5):
        print(f"number:-{i}")
        time.sleep(4)

def func2():
    for k in "ABCDE":
        print(f"Letter:-{k}")
        time.sleep(4)

if __name__=="__main__":
    start_time=time.time()
    t1=threading.Thread(target=func1)
    t2=threading.Thread(target=func2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end_time=time.time()
    total_time=end_time-start_time
    print(f"Total execuation time;-{total_time}")

import copy
ls1=[1,2,3,4,["first","second"]]
ls2=ls1.copy()
ls2[4][0]="hundred"
print(f"this is ls2 list{ls2}")
print(f"this is ls1 automatic reflect value{ls1}")

from copy import deepcopy
ds1={"a":[10,20,30],"b":[100,200,300,(10000000,2000000000)],"c":{1000,4000,2000},"d":{"name":"shri","age":27}}
ds2=deepcopy(ds1)
ds2["b"][3]=1111111111111111111111
print(ds1)
print(ds2)

add_func=lambda x:x+10
ls1=[1,2,3,4,5]
print(list(map(add_func,ls1)))

def outer_func(x):
    def inner_func(y):
        return x+y
    return inner_func
closure=outer_func(10)
print(closure(5))

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_all(self,location):
        self.location=location
        return f"this is my name-{self.name} and age-{self.age} and this is my location-{self.location}"

    def first_method(self,location):
        print("this self parmeter access the show_all method")
        self.location=location
        result=self.show_all(location)
        return result
obj1=Person("shri",27)
print(obj1.first_method("indore"))

class Car(object):
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand

    def show_info(self):
        return f"This is my response:-{self.brand}-{self.model}"

obj1=Car("indica","TaTa")
print(obj1.show_info())
obj2=Car("Bolero","mahindra")
print(obj2.show_info())

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area():
        pass
    @abstractmethod
    def parameter():
        pass

class Circle(Shape):
    a=10
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.a

    def parameter(self):
        return 2*3.14*self.radius

obj1=Circle(100)
print(obj1.area())
print(obj1.parameter())

class Person(object):
    name=str(input("Enter a name"))
    def __init__(self,age,location):
        self.age=age
        self.location=location

    def fetch_all_attribute_method(self):
        return f"this is person name{self.name} and age will be{self.age} and this person from{self.location}"
    
obj1=Person(24,"indore")
print(obj1.fetch_all_attribute_method())

class Car(object):
    def __init__(self,model,year,company):
        self.model=model
        self.year=year
        self.company=company

    def instance_method(self):
        return f"this is my car {self.model} and this year will lanuch is {self.year} and created this company{self.company}"

instance1=Car("bolero",2011,"mahindra")
print(instance1.company)
print(instance1.instance_method())
        
from abc import ABC,abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def initiate_payment(self,amount):
        pass

    @abstractmethod
    def verify_transaction(self,transaction_id):
        pass

class CreditCardPayment(PaymentProcessor):
    def initiate_payment(self,amount):
        print(f"Processing credit card payment of ${amount}")

    def verify_transaction(self,transaction_id):
        print(f"Verifying credit card transaction {transaction_id}")

class PayPalPayment(PaymentProcessor):
    def initiate_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
    
    def verify_transaction(self, transaction_id):
        print(f"Verifying PayPal transaction {transaction_id}")

payment1=CreditCardPayment()
payment1.initiate_payment(100)
payment1.verify_transaction(457548574875)

class Person(object):
    def __new__(cls,*args,**kwargs):
        print("Creting the new instance")
        instance=super().__new__(cls)
        return instance
    
    def __init__(self,name):
        print("Intilizing the instance")
        self.name=name

obj1=Person("shrikant")
print(obj1.name)

class Person(object):
    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs

    def show_result(self):
        for value in self.args:
            print(f"this is values:-{value}")
ls1=["shrikant","ajay"]
ds1={"name":"rahul","age":27}
obj1=Person(ls1,ds1)
obj1.show_result()

class Animal(object):
    def __init__(self,species):
        self.species=species

    def make_sound(self):
        return f"Some Generice animal sound"
    
class Dog(Animal):
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def make_sound(self):
        result=super().make_sound()
        print(f"Woof:-{result}")

obj1=Dog("pitbull","tommy")
obj1.make_sound()
