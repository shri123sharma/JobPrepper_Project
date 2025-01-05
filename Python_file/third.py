class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        print(f"User Initialized: {self.name}, {self.email}")

    def get_user_detail(self):
        return {"Name": self.name, "Email": self.email}
    
class Customer(User):
    def __init__(self,name,email,cart):
        super().__init__(name,email)
        self.cart=cart
        print(f"Customer Initialized: Cart={self.cart}")

    def add_to_cart(self,product):
        self.cart.append(product)
        print(f"{product} added to cart")

class Admin(User):
    def __init__(self,name,email,permissions):
        super().__init__(name,email)
        self.permissions=permissions

    def manage_product(self,product,action):
        print(f"Admin {action}s the product: {product}")

customer = Customer("Alice", "alice@example.com", [])
admin = Admin("Bob", "bob@example.com", ["add_product", "remove_product"])

customer.add_to_cart("test_product")

from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @abstractmethod
    def get_role(self):
        pass

class Customer(User):
    def get_role(self):
        return "this is get role"

obj1=Customer("test_user",24)
print(obj1.get_role())

import time
start_time=time.time()
t1=tuple(range(100))  
for k in t1:
    print(f"item:-{k}")

end_time=time.time()
Total=end_time-start_time
print(f"tuple objects one lakh iteration time {Total}")


import time
start_time=time.time()
l1=list(tuple(range(100)))
for j in l1:
    print(f"item:-{j}")

end_time=time.time()
Total=end_time-start_time
print(Total)

