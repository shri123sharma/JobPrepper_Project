def decorator_func(func):
    def wrapper(a,b,*args,**kwargs):
        print("This is before the calling")
        # result=a+b
        result=func(a,b)
        return f"this is result:-{result}"
        print(f"Add the two value and result",result)
        print("This is after the calling func")
    return wrapper
@decorator_func
def func(a,b):
    return a+b

result=func(10,20)
print(result)

import time
def time_measure_decorator(func):
    def wrapper(*args,**kwargs):
        print("Before calling the function")
        start_time=time.time()
        result=func()
        end_time=time.time()
        total_time=end_time-start_time
        return f"this function result for:-{result}-{total_time}"
    return wrapper

@time_measure_decorator
def func():
    sum=0
    for i in range(1,10):
        sum+=i
    return sum

result=func()
print(result)

import threading
import time

def number_func():
    for i in range(1,5):
        print(f"this is numbers iterate:-{i}")

def letter_func():
    for j in "ABCDEF":
        print(f"this is letters iterate:-{j}")

if __name__=="__main__":
    t1=threading.Thread(target=number_func)
    t2=threading.Thread(target=letter_func)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def outer_func(a):
    def inner_func(b):
        result=f"this is both value added:-{a+b}"
        return result
    return inner_func

result=outer_func(10)
print(result(20))

is_even=lambda x:x%2==0
for i in range(1,10):
    if is_even(i)%2==0:
        print(f"this is even number{i}")
    else:
        print(f"this is Odd number{i}")


func_add=lambda a,b,c:a+b+c
result=func_add(10,20,30)
print(result)

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def method_1(self):
        return f"This is method-1 and instance attribute:-{self.name}-{self.age}"
    
obj1=Person("testing",23)
print(obj1.method_1())


global sum_val
def add_func(n):
    sum_val+=n
    return sum_val

if __name__=="__main__":
    number=[1,2,3,4,5,6]
    result=list(map(add_func,number))
    print(result)

class GrandFather(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def method_1(self):
        return f"this method-1 show{self.name}-{self.age}"

class Father(GrandFather):
    def __init__(self,name,age,location):
        super().__init__(name,age)
        self.location=location

    def method_2(self):
        return f"this method-2 show{self.name}-{self.age}-{self.location}"

obj1=Father("test",24,"indore")
print(obj1.method_1())

import sys

a=[1,2,3,4,5,5]
print("Refrennce count of a",sys.getrefcount(a))

b=a
print("Referece count of b",sys.getrefcount(b))

import gc
var=gc.collect(a)
print(var)

ls1=[1,200,{"name":"shri"},{1,2,1,2,1,2},("hello","World")]
print(ls1)
ls1.append("this is list")
print(ls1)

from array import array
arr=array("1",[1,2,3,4,5,6,7])
arr.append(100)
print(arr)

t1=(1,2,{"name":"hello"},(100,200,300),["hello","world"])
t1[1]=1000000
print(t1)

class Father(object):
    def __init__(self,father_name,**kwargs):
        super().__init__(**kwargs)
        self.father_name=father_name

    def father_method(self):
        return f"this is father method {self.father_method}"
    
class Mother(object):
    def __init__(self,mother_name,**kwargs):
        super().__init__(**kwargs)
        self.mother_name=mother_name

    def mother_method(self):
        return f"this is mother method:-{self.mother_name}"
    
class Child(Father,Mother):
    def __init__(self,father_name,mother_name,location):
        super().__init__(father_name=father_name,mother_name=mother_name)
        self.location=location

    def child_method(self):
        return f"this is child method {self.father_name}-{self.mother_name}-{self.location}"
    
child_obj=Child("testing_father","testing_mother","indore")
print(child_obj.child_method())

class Person(object):
    def bark(self):
        return "this is bark"
    
def bark_modified(self):
    return "this is bark_modified"

Person.bark=bark_modified
obj1=Person()
print(obj1.bark())

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @property
    def method1(self):
        return "this is method but its consider as a attribute"
    
obj1=Person("test",23)
print(obj1.method1)
