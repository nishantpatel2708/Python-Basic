# class Phone:
#     def __init__(self,model_name,com_name,_price):
#         self.model_name=model_name
#         self.com_name=com_name
#         self._price=_price
#     def full_name(self):
#         return f"THis is model name{self.model_name} and com name is {self.com_name}"
# class Smartphone(Phone):
#     def __init__(self, model_name, com_name, _price,cam,ram):
#         # super().__init__(model_name, com_name, _price)
#         Phone.__init__(self,model_name, com_name, _price)
#         self.cam=cam
#         self.ram=ram
#     def full_name(self):
#          return f"THis is model name{self.model_name} and com name is {self.com_name} {self.ram}"
# S1=Smartphone('m11','Samsung',6000,'2mp','4gb')
# print(S1.full_name())
# class Phone:
#     def __init__(self,model_name,com_name,_price):
#         self.model_name=model_name
#         self.com_name=com_name
#         self._price=_price
#     def full_name(self):
#         return f"THis is model name{self.model_name} and com name is {self.com_name}"
# class Smartphone(Phone):
#     def __init__(self, model_name, com_name, _price,cam,ram):
#         super().__init__(model_name, com_name, _price)
#         # Phone.__init__(self,model_name, com_name, _price)
#         self.cam=cam
#         self.ram=ram
#     def full_name(self):
#         return f"THis is model name{self.model_name} and com name is {self.com_name} {self.ram}"
# class Flegshipphone(Smartphone):
#     def __init__(self, model_name, com_name, _price, cam, ram,r_cam):
#         super().__init__(model_name, com_name, _price, cam, ram)
#         self.r_cam=r_cam
#     def full_name(self):
#          return f"THis is model name{self.model_name} and com name is {self.com_name} {self.ram} {self.r_cam}"
# S1=Smartphone('m11','Samsung',6000,'2mp','4gb')
# F1=Flegshipphone('n11','Nokia',10000,'4mp','8gb','7mp')
# # print(F1.full_name())
# print(help(Flegshipphone))

# class A:
# class B:
# class C(A,B)
# temp=0
# l=[{'a':1,'b':2,'c':3},{'a':2,'c':4},{'a':3,'b':4,'c':5}]
# for i in l:

#     for j in i:
#         if j in i:
#             print(j)
# for i in l:
#     keys1=i.keys()
# print(keys1)
#     for j in l:
#         print([keys1[j]])


# class Father:
#     def __init__(self,name,age,property):
#         self.name=name
#         self.age=age
#         self.property=property
#     def full_name(self):
#         return f"This is my father details {self.age} {self.name} {self.property}"
# class Son(Father):
#     def __init__(self, name, age, property,skin):
#         super().__init__(name, age, property)
#         self.skin=skin
#     def full_name(self):
#         return f"This is my son details {self.age} {self.name} {self.property} {self.skin}"
# F1=Father('Rajesh',56,'2bhk')
# # print(F1.full_name())
# S1=Son('Chirag',28,'3bhk','lightdark')
# print(S1.full_name())
# print(S1)
# print(F1)
#method resolution order
# print()

# Examples of Inheritance
# A --> B --> C siglelevel inheritance
# class Car1:
#     def __init__(self,model_name,company,price,petrol):
#         self.model_name=model_name
#         self.company=company
#         self.price=price
#         self.petrol=petrol
#     def fuel(self):
#         return f"The {self.company}'s {self.model_name} is coasted at {self.price} and which runs on {self.petrol}"

# class Car2(Car1):
#     def __init__(self,model_name,company,price,petrol,diesel):
#         super().__init__(model_name,company,price,petrol)
#         self.diesel=diesel
#     def fuel(self):
#         return f"The {self.company}'s {self.model_name} is coasted at {self.price} and which runs on {self.petrol} and also {self.diesel}"

# class Car3(Car2):
#     def __init__(self, model_name, company, price, petrol, diesel, CNG):
#         super().__init__(model_name, company, price, petrol,diesel)
#         self.CNG=CNG
#     def fuel(self):
#         return f"The {self.company}'s {self.model_name} is coasted at {self.price} and which runs on {self.petrol} and {self.diesel} and also {self.CNG}"


# C1=Car1('Triber', 'Renault',775000,'petrol')
# print(C1.fuel())
# C2=Car2('Triber', 'Renault',775000,'petrol','diesel')
# print(C2.fuel())
# C3=Car3('Triber', 'Renault',775000,'petrol','diesel','CNG')
# print(C3.fuel())

# A --> C <-- B Example 2
# from this import d


class Car1:
    def __init__(self,model_name,company,price,petrol):
        self.model_name=model_name
        self.company=company
        self.price=price
        self.petrol=petrol
    def fuel(self):
        return f"The {self.company}'s {self.model_name} is coasted at {self.price} and which runs on {self.petrol}"

class Car2():
    def __init__(self,model_name,company,price,diesel):
        self.model_name=model_name
        self.company=company
        self.price=price
        self.diesel=diesel
    def fuel(self):
        return f"The {self.company}'s {self.model_name} is coasted at {self.price} and which runs on {self.diesel}"

class Car3(Car1,Car2):
    def __init__(self, model_name, company, price, petrol, diesel, CNG):
        # super().__init__(model_name, company, price, petrol)
        # super().__init__(model_name, company, price, diesel)
        
        Car1.__init__(self,model_name, company, price, petrol)
        Car2.__init__(self,model_name, company, price, diesel)
        self.CNG=CNG

    def __add__(self,other):
        return self.price+other.price

    def fuel(self):
        return f"The {self.company}'s {self.model_name} is coasted at {self.price} and which runs on {self.petrol} and {self.diesel} and also {self.CNG}"
    
    # def __str__(self):
    #     return f"The {self.company}'s {self.model_name} is coasted at {self.price} and which runs on {self.petrol} and {self.diesel} and also {self.CNG}"

    # def __repr__(self):
    #     return f"The {self.company}'s {self.model_name} is coasted at {self.price} and which runs on {self.petrol} and {self.diesel} and also {self.CNG}"

C1=Car1('Triber', 'Renault',775000,'petrol')
print(C1.fuel())
C2=Car2('Triber', 'Renault',775000,'diesel')
print(C2.fuel())
C3=Car3('Triber', 'Renault',775000,'petrol','diesel','CNG')
C4=Car3('Triber', 'Renault',775000,'petrol','diesel','CNG')

# print(C3.fuel())
# print(C3)
print(C3+C4)
# print(isinstance(C2,Car1))
# print(issubclass(Car2,Car2))

# class Car1:
#     def __init__(self,model_name,company,price):
#         self.model_name=model_name
#         self.company=company
#         self.price=price
#     def fuel(self):
#         return f"The {self.company}'s {self.model_name} is coasted at {self.price}"

# class Car2(Car1):
#     def __init__(self,model_name,company,price,seater_5):
#         super().__init__(model_name, company, price)
#         self.seater_5=seater_5
#     def fuel(self):
#         return f"The {self.company}'s {self.model_name} is coasted at {self.price} and which is {self.seater_5}"

# class Car3(Car1):
#     def __init__(self, model_name, company, price, seater_7):
#         super().__init__(model_name, company, price)
#         self.seater_7=seater_7
#     def fuel(self):
#         return f"The {self.company}'s {self.model_name} is coasted at {self.price} and which is {self.seater_7}"


# C1=Car1('Triber', 'Renault',775000,)
# print(C1.fuel())
# C2=Car2('Triber', 'Renault',775000,'seater_5')
# print(C2.fuel())
# C3=Car3('Triber', 'Renault',775000,'seater_7')
# print(C3.fuel())