# Encalpultion
class Person:              #class define
    def __init__(self,fname,lname,age,id=None):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.id=id
    def full_name(self,mname):
        return f"Your first name is {self.fname} and your mname is {mname} your last name is {self.lname} id is {self.id}"
    def is_above_18(self):
        if self.age>18:
            return True
        else:
            return False
P1=Person('cirag','joshi',58)
class Phone:
    def __init__(self,model_name,com_name,_price):
        self.model_name=model_name
        self.com_name=com_name
        self._price=_price
    def full_name(self):
        return f"THis is model name{self.model_name} and com name is {self.com_name}"
class Smartphone(Phone):
    def __init__(self, model_name, com_name, _price,cam,ram):
        super().__init__(model_name, com_name, _price)
        # Phone.__init__(self,model_name, com_name, _price)
        self.cam=cam
        self.ram=ram
    def full_name(self):
        return f"THis is model name{self.model_name} and com name is {self.com_name} {self.ram}"
class Flegshipphone(Smartphone):
    def __init__(self, model_name, com_name, _price, cam, ram,r_cam):
        super().__init__(model_name, com_name, _price, cam, ram)
        self.r_cam=r_cam
    def full_name(self):
         return f"THis is model name{self.model_name} and com name is {self.com_name} {self.ram} {self.r_cam}"
S1=Smartphone('m11','Samsung',6000,'2mp','4gb')
F1=Flegshipphone('n11','Nokia',10000,'4mp','8gb','7mp')
# print(F1.full_name())
print(help(Smartphone))


