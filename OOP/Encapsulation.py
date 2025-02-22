                    # Encapsulation
                    
# by using Encapsulation we can restrict the variable and methods access by making it private and protected

# In encapsulation, the internal state of an object is kept hidden and can only be accessed or modified through the defined methods or properties of the object. 

    # This allows for better control and organization of code, as well as providing data abstraction and information hiding.
    #  NOTE: alomst every class which uses private and protected methods are Encapsulation classes.


class A:
    _a = 10
    __b = 20
    c = 50
    def show(self):
        print("a=", self._a, "b=", self.__b, "c=", self.c)

obj = A()
obj.c = 0
obj.__b = 3000   # can not change outside class
obj.show()

    