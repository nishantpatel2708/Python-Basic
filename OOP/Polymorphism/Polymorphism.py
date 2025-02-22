                    # Polymorphism 
    # Polymorphism ability to take various forms
    # same object having different behaviors called Polymorphism 
    
    
# Example:
print(5 + 5)
print("5" + "5")



            # Method Overloading
    # whenever class contains more than one method with same name and different types parameters call Method Overloading

# # Example:

# class A:
#     def Show(self):
#         print("Welcome")
#     def Show(self, fname= ''):
#         print("welcome", fname)
#     def Show(self, fname= '', lname=''):
#         print("welcome", fname, lname)
    
# obj = A()
# obj.Show()
# obj.Show("Nishant")
# obj.Show("Nishant", "Patel")


            # Method Overriding
    # whenever we write method name with same signature in parent and child class called Method Overriding
    # note: wihtout inheritance we cannot peform Method Overriding

# Example:

class A():
    def disp(self):
        print("This is parent class")

class B(A):
    def disp(self):
        print("This is child class")

obj = B()
obj.disp()  # here we override the parent class function with same name.