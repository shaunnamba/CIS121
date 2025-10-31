class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_price(self):
        return self.price
    def set_price(self,price):
        self.price=price
    def get_quantity(self):
        return self.quantity
    def set_price(self,quantity):
        self.quantity=quantity

product1=Product("fish",20,2)


class Book:
    def __init__(self,title,author,page_count):
        self.title=title
        self.author=author
        self.page_count=page_count
    def get_title(self):
        return self.title
    def set_title(self,title):
        self.title=title
    def get_author(self):
        return self.author
    def set_author(self,author):
        self.author=author
    def get_page_count(self):
        return self.page_count
    def set_page_count(self,page_count):
        self.page_count=page_count

book1=Book("harry pooter","auth",34)

class Employee:
    def __init__(self,name,title,salary):
        self.name=name
        self.title=title
        self.salary=salary
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_title(self):
        return self.title
    def set_title(self,title):
        self.title=title
    def get_salary(self):
        return self.salary
    def set_name(self,salary):
        self.salary=salary
    
    def greeting(self):
        return f"Hello. My name is {self.name}. I'm the {self.title}"
    def request_raise(self):
        new_salary= self.salary*1.06
        return f"I’m currently making ${self.salary}. I’d like new salary of ${new_salary}."

class Student:
    def __init__(self,name,major,gpa):
        self.name=name
        self.major=major
        self.gpa=gpa
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_major(self):
        return self.major
    def set_major(self,major):
        self.major=major
    def get_gpa(self):
        return self.gpa
    def set_name(self,gpa):
        self.gpa=gpa

    def introduce(self):
        return f"Hi, I'm {self.name}. I'm studying {self.major}"
    def study_for_exam(self):
        old_gpa = self.gpa
        new_gpa = old_gpa+0.2
        return f"Im hitting the books! My GPA increased for {old_gpa} to {new_gpa}"
 
student1=Student("jeff","cis",3.5)
print(student1.study_for_exam())












# class Candy:
#     def __init__(self):
#         self.name="unknown"
#         self.flavor="unknown"
#         self.size="unknown"
#         self.price="unknown"
#         self.shape="unknown"
#     def get_name(self):
#         return self.name
#     def set_name(self,value):
#         self.name=value

#     def get_flavor(self):
#         return self.flavor
#     def set_flavor(self,value):
#         self.flavor=value

#     def get_size(self):
#         return self.size
#     def set_size(self,value):
#         self.size=value

#     def get_price(self):
#         return self.size
#     def get_price(self):
#         return self.price* 1.4
#     def set_price(self,value):
#         if 0<=value<1000:
#             self.price=value
    
#     def get_shape(self):
#         return self.shape
#     def set_shape(self,value):
#         self.shape=value

#     def reaction(self):
#         if 0<self.size<5:
#             return "try again next time"
#         elif 5<self.size<10:
#             return "Ehh is gues its okay"
#         else:
#             "WoW"
    
#     def __str__(self):
#         return f"{self.name} its {self.flavor} costs {self.price} and the size and shape is {self.size}, {self.shape} {self.reaction()}"
    
# candy1=Candy()
# candy1.set_name("Kitkat")
# candy1.set_shape("square")
# candy1.set_flavor("chocolate")
# candy1.set_size(10)
# print(candy1.())
        
        
        