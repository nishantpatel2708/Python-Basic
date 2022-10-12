def pathik(a,b):
    return a+b 
a=int(input("Enter your value::"))
b=int(input("Enter your value::"))

print(pathik(a,b))
# print(add_two("chirag",5))
# return vs print()
def add_two(a,b):
    print(a+b)
print(add_two(4,5))

add_two(2,4)


# def patt():
#     for i in range(5):
#         for j in range(i):
#             print('* ',end='')
#         print()
# patt()

# name=input("Enter your name::")
# def last_char(name1):
#     return name1[-1]
# print(last_char(name))

# def odd_even(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(odd_even(6))
# def greter(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(greter(4,5))
# def gretest(a,b,c):
#     if a>b and a>c:
#         return a 
#     elif b>a and b>c:
#         return b 
#     else:
#         return c
# def gretest(a,b,c):
#     temp=greter(a,b)
#     return greter(temp,c)
# print(gretest(15,6))


# def user_info(name,age):

#         # python2
#         name="chirag"
#         age=76
#         print("Your name is "+name+" and yor age is"+str(age))
#         print("your name is {} and your age is {}".format(name,age))
#         print(f"Your name is {name} and your age is {age}")

# def user_info(name='unknow',age=None):
#         return f"your name is {name} and your age is {age}"

#         print(user_info('chirag'))
