class Student:
    def __init__(self,name,major):
        self.name=name
        self.major=major
    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name=new_name
    def get_major(self):
        return self.major
    def set_major(self,new_major):
        self.major=new_major
    def __str__(self):
        return f'My name is {self.name} and my major is {self.major}'
    
class Course:
    def __init__(self,course_name,course_number):
        self.students=[]
        self.name=course_name
        self.number=course_number
    def get_number(self):
        return self.number
    def set_number(self,new_number):
        self.number=new_number
    def add_student(self,student):
        self.students.append(student)
    def show_students(self):
        for student in self.students:
            print(student) 
    def __str__(self):
        return f'Course name: {self.name}, Course number: {self.number}'
    
course1=Course('intro to prog',"Cs121")
student1=Student('Ashley','Computer Science')
student2=Student('jeff','comms')


course1.add_student(student1)
course1.add_student(student2)
print(course1)
course1.show_students()




class Duck:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name=new_name
    def get_color(self):
        return self.color
    def set_color(self,new_color):
        self.color=new_color
    def speak(self):
        print("quack")
    def __str__(self):
        return f'the name is {self.name} and the color is {self.color}'

class Pond:
    def __init__(self,name):
        self.ducks=[]
        self.name=name
    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name=new_name
    def add_ducks(self,duck):
        self.ducks.append(duck)
    def quaks(self):
        for duck in self.ducks:
            print(f'{duck.name} says: ')
            duck.speak()
    def __str__(self):
        return f"Pond name: {self.name}, Number of ducks: {len(self.ducks)}"
        
pond1=Pond('breezy')
duck1=Duck('quakky','blue')
duck2=Duck('cole','red')

pond1.add_ducks(duck1)
pond1.add_ducks(duck2)
print(pond1)

pond1.quaks()


# class Lion:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
#     def get_name(self):
#         return self.name
#     def set_name(self,new_name):
#         self.name=new_name
#     def get_gender(self):
#         return self.gender
#     def set_gender(self,new_gender):
#         self.gender=new_gender
#     def roar(self):
#         print('Roar')
#     def __str__(self):
#         return f'The name is {self.name} and the gender is {self.gender}'


# class Zoo:
#     def __init__(self,location):
#         self.lions=[]
#         self.location=location
#     def add_lion(self,lions):
#         self.lions.append(lions)
#     def lions_roar(self):
#         for lion in self.lions:
#             print(f'{lion.name} ',end='')
#             lion.roar()
#     def count_lions(self):
#         male=0
#         female=0
#         for lion in self.lions:
#             if lion.gender=="male":
#                 male+=1
#             elif lion.gender=="female":
#                 female+=1
#         print(f'{male} male,{female} female.')
#     def __str__(self):
#         return f'Zoo location: {self.location}, number of lions {len(self.lions)}'
        
        
# zoo1=Zoo('Minnesota')
# lion1=Lion('jeff','male')
# lion2=Lion('molly','female')
# lion3=Lion('sjjs','female')
# zoo1.add_lion(lion1)
# zoo1.add_lion(lion2)
# zoo1.add_lion(lion3)
# print(zoo1)
# zoo1.lions_roar()
# zoo1.count_lions()



# class Employee:
#     def __init__(self,name,position):
#         self.name=name
#         self.position=position
#     def get_name(self):
#         return self.name
#     def set_name(self,new_name):
#         self.name=new_name
#     def get_position(self):
#         return self.position
#     def set_position(self,new_position):
#         self.position=new_position
#     def __str__(self):
#         return f'my name is {self.name} and my position is {self.position}'


# class Department:
#     def __init__(self,dept_name,budget):
#         self.name=dept_name
#         self.budget=budget
#         self.employees=[]
#     def get_budget(self):
#         return self.budget
#     def set_budget(self,new_budget):
#         self.budget=new_budget
#     def add_employees(self,employees):
#         self.employees.append(employees)
#     def show_staff(self):
#         for employee in self.employees:
#             print(employee)
#     def is_large(self):
#         return len(self.employees) >10
#     def __str__(self):
#         return f'{self.name} budget is {self.budget} and has {len(self.employees)} employees'
    
# dept1=Department('hr',2000)
# employee1=Employee('jeff','AP')
# empolyee2=Employee('lisa','front end')
# dept1.add_employees(employee1)
# dept1.add_employees(empolyee2)
# print(dept1)
# dept1.show_staff()
# print(dept1.is_large())



# class Droid:
#     def __init__(self,designation,series):
#         self.designation=designation
#         self.series=series
#     def get_name(self):
#         return self.series
#     def set_series(self,new_series):
#         self.series=new_series
#     def comms(self):
#         print('Beep-Blopp-Blop')
#     def __str__(self):
#         return f'Designation: {self.designation}, Series: {self.series}'
    
# class Starship:
#     def __init__(self,name):
#         self.name=name
#         self.droids=[]
#     def add_droids(self,droids):
#         self.droids.append(droids)
#     def all_comms(self):
#         for droid in self.droids:
#             print(f'{droid.designation} says: ',end='')
#             droid.comms()
#     def __str__(self):
#         return f'Name: {self.name} droids: {len(self.droids)}'

# starship1=Starship("Unistar")
# droid1=Droid("4r-5t","NewGen")
# droid2=Droid("57-df","2.0new")
# starship1.add_droids(droid1)
# starship1.add_droids(droid2)
# print(starship1)
# starship1.all_comms()





# class Post:
#     def __init__(self,caption,likes):
#         self.caption=caption
#         self.likes=likes
#     def get_likes(self):
#         return self.likes
#     def set_likes(self,new_likes):
#         self.likes=new_likes
#     def add_like(self):
#         self.likes+=1
#     def display(self):
#         print(f"Caption: {self.caption}")
#     def __str__(self):
#         return f'the posts caption is: {self.caption} and the has {self.likes} likes.'

# class Profile:
#     def __init__(self,username):
#         self.name=username
#         self.posts=[]
#     def add_post(self,posts):
#         self.posts.append(posts)
#     def is_trending(self):
#         trending=False
#         for post in self.posts:
#             if post.get_likes()>=10000:
#                 post.display()
#                 trending =True
#     def __str__(self):
#         return f'Profile: {self.name} ,Posts: {len(self.posts)}'
    
# profile1=Profile('james34')
# post1=Post('daily dump',10000)
# post2=Post('monthly dump',8888)
# profile1.add_post(post1)
# profile1.add_post(post2)
# print(profile1)
# profile1.is_trending()


# class ShoppingCart:
#     def __init__(self,customer_id):
#         self.id=customer_id
#         self.products=[]
#     def add_product(self,products):
#         self.products.append(products)
#     def calculate_total(self):
#         for product in self.products:
#             total=0
#             total+=product.get_price()
#         return total

# class AICompany:
#     def __init__(self,name,year,headquarters):
#         self.name=name
#         self.year=year
#         self.headquarters=headquarters
#         self.llms=[]
#     def get_headquarters(self):
#         return self.headquarters
#     def set_headquaters(self,new_headquarters):
#         self.headquarters=new_headquarters
#     def add_llm(self,llms):
#         self.llms.append(llms)
#     def display_models(self):
#         for llm in self.llms:
#             print(llm)


# class Restaurant:
#     def __init__(self,name):
#         self.name=name
#         self.menu_items=[]
#     def add_menu_items(self,items):
#         self.menu_items.append(items)
#     def display_menu(self):
#         for item in self.menu_items:
#             reduced=item-2
#             print()


class Vector:
    def __init__(self, )