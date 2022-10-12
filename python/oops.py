# Class? 
# class blueprint 
# class blueprint 
# class Person:              #class define
#     def __init__(self,fname,lname,age,id=None):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#         self.id=id
#     def full_name(self,mname):
#         return f"Your first name is {self.fname} and your mname is {mname} your last name is {self.lname} id is {self.id}"
#     def is_above_18(self):
#         if self.age>18:
#             return True
#         else:
#             return False

# p1=Person('chirag','joshi',85)
# print(p1.is_above_18())
# print(p1.full_name('Rajeshbhai'))
#instance method

# class Variable 

# class Circle:
#     def __init__(self,pi,radius):
#         self.pi=pi
#         self.radius=radius
#     def cal_circumference(self):
#         return 2*self.pi*self.radius  

# C1=Circle(3.14,5)
# C2=Circle(3.14,10)

# print(C1.cal_circumference())
# print(C2.cal_circumference())
# class Circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def cal_circumference(self):
#         return 2*Circle.pi*self.radius
# r=int(input("Enter radius::"))
# C1=Circle(r)

# print(C1.cal_circumference())
# Class method 
# class Person:#class define
#     count=0
#     def __init__(self,fname,lname,age):
#         Person.count+=1
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     @classmethod  
#     def count_instance(cls):
#         return f"you have created object {cls.count}"
# p1=Person('chirag','joshi',85)
# p2=Person('chirag','joshi',85)

# print(Person.count_instance())

#class method as constrctor
class Person:#class define
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def full_name(self):
        return f"Your first name is {self.fname} and  your last name is {self.lname}"
    @classmethod
    def from_string(cls,string):
        fname,lname,age=string.split()
        return cls(fname,lname,age)
P3=Person.from_string("Chirag joshi 90")
print(P3.full_name())
print(P3.fname)


# class Person:#class define
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     def full_name(self):
#         return f"Your first name is {self.fname} and  your last name is {self.lname}"
#     #define
#     @staticmethod
#     def hello():
#         print("Hello i am static method")
# Person.hello()
# Person.full_name()


# Inheritance method
# class A:
#     def __init__(self,name,age,village):
#         self.name=name
#         self.age=age
#         self.village=village
#     def fullname(self):
#         return f"Hello, My I'm {self.name}. I'm {self.age} years old and I'm from {self.village}"

# a1=A('Axar',29,'Rajkot')
# print(a1.fullname())

# # class variable 
# class X:
#     def __init__(self,n):
#         self.n=n
#     def total(self):
#         return self.n*(self.n+1)/2
# n=int(input("Enter number : "))
# x1=X(n)
# print(x1.total())

# # Area of circle
# class Circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 2*Circle.pi*self.radius

# radius=int(input("Enter radius : "))
# c1=Circle(radius)
# print(c1.area())

# class method
# class A:
#     count=0
#     def __init__(self,name,age,village):
#         self.name=name
#         self.age=age
#         self.village=village
#         A.count+=1
#     @classmethod
#     def counter(cls):
#         return f"Total number of printing strings {cls.count}"
    
# a1=A('Rohit',45,'Sharma')
# a2=A('Virat',18,'Kohli')
# print(A.counter())

# class method as a constructor
# class A:
#     def __init__(self,city,pin):
#         self.city=city
#         self.pin=pin
#     def pair(self):
#         return f"My city is {self.city} and it's pincode is {self.pin}"

#     @classmethod
#     def address(cls,string):
#         city,pin=string.split(' ')
#         return cls(city,pin)
# a1=A.address('Ahmedabad 380050')
# print(a1.pair())

# static method
class A:
    def __init__(self,car_name,price):
        self.car_name=car_name
        self.price=price
    def info(self):
        return f"This is {self.car_name} and it's price is {self.price}"

    @staticmethod
    def details():
        print("This is luxurious car")

A.details()





