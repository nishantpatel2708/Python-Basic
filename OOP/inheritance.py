        # Python Inheritance
# When we define a class that inherits all the properties of other class called inheritance.

# class Father:
#     def Lands(self):
#         print("Having 50 Eker land")
    
# class Son(Father):
#     def Money(self):
#         print("Having 10 Lakhs of money")

# s = Son()
# s.Lands()
# s.Money()


        ## Simple Inheritance
# class A:
#     num1 = int(input("Enter 1st number:"))
#     num2 = int(input("Enter 2st number:"))

#     def add(self):
#         print("Add", self.num1 + self.num2)
#     def sub(self):
#         print("Sub", self.num1 - self.num2)

# class B(A):
#     def Mul(self):
#         print("Mul", self.num1 * self.num2)
#     def Div(self):
#         print("Div", self.num1 / self.num2)

# obj = B()
# obj.add()
# obj.sub()
# obj.Mul()
# obj.Div()


        ## Multi level Inheritance
    # In this inheritance we have one parent and multiple child classes
    
# class Father:
#     surname = "Patel"

# class Son(Father):
#     def Show(self):
#         print("Arvindbhai", self.surname)

# class Gson(Son):
#     def Dis(self):
#         print("Nishant ", self.surname)
        
# S = Son()
# S.Show()

# Gs = Gson()
# Gs.Dis()
# Gs.Show()


        ## Multiple Inheritance
    # Inheritance Which contains more parent classes and one child class is called multiple inheritance
    
# class Nishant:
#     back = "django & MySQL"
#     def backend(self):
#         print("Backend Work Done using", self.back)

# class Anand:
#     front = "HTML CSS JS"
#     def frontend(self):
#         print("Frontend Work Done using", self.front)

# class TeamLead(Nishant, Anand):
#     def Show(self):
#         print("Website Created....")


# obj = TeamLead()
# obj.backend()
# obj.frontend()
# obj.Show()


        ## hierarchical inheritance 
    
    # inheritance which contain only one parent class and multiple child classes but each child class can access parent class properties.
    
