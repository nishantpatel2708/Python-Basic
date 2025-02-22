def my_fuc():
    print("this is fuction")
    print('this is second function')

my_fuc()


def my_name(name):
    print("Your name is", name)

my_name('Nishant')


def default_name(name="anand"):
    print("Name: ",name)
default_name()
default_name("nishant")


def plus(a, b):
    print("sum of a and b is",a+b)
plus(5, 7)


def plus(a, b):
    print("sum of a and b is",a+b)
    return a+b
print(plus(5, 7))


def new_fun(*car):
    print(car)
    print("Car Name is:",car[0])
new_fun("Toyota", "Kia", "Ford")



def names(**nm):
    print(nm)
names(fname="Nishant", Lname="Patel")

