a = int(input('Enter First number: '))
b = int(input('Enter Second number: '))

if a > b :
    print(a,'is bigger then',b) 
    
elif a < b :
    print(a,'is smaller then',b)

elif a == b:
    print(a,'is same as',b)

else:
    print('wrong input')


# --------------------------------------------

a = int(input('Enter any number:' ))

if a <= 100:
    if a <=50:
        print(a,'is between 1 to 50')
        if(a%2 == 0):
            print("it is Even")
        else:
            print("it is Odd")
    else:
        print(a,'is between 50 to 100')
        if(a%2 == 0):
            print("it is Even")
        else:
            print("it is Odd")
else:
    print('Wrong input')


# --------------------------------------------




var = input("Enter name: ")

bird = ["sparrow", "peacock", "owls", "swift", "strok" ]
animal = ["lion", "tiger", "dog", "horse", "cat"]
total = bird + animal

if var in total:
    for i in total:
        if i == var:
            if i in animal:
                print("this is animal")
            else:
                print("this is bird")
else:
    print("Wrong input")


# --------------------------------------------



VAR = int(input("enter the number: "))
A = [1,3,5,7,9]
B = [2,4,6,8]
C = [1,2,3,4,5,6,7,8,9]

if VAR in C:
    for i in C:
        if i == VAR:
            if i in A:
                print("the number is in A")
                if i % 2 == 0:
                    print(i,"number is even")
                elif i != 0:
                    print(i,"number is odd")
             
            elif i in B:
                print(i,"number is in B ")
                if i %2 == 0:
                    print(i,"number is even")
                elif i != 0:
                    print("the number is odd")
else:
    print(" wrong input")



# --------------------------------------------


name = input('enter name: ')
ani = ['dog','cat','lion']
bir = ['sparrow','cock','dove']
all = ['dog','cat','lion','sparrow','cock','dove']
if name in all:
    for i in all:
        if i==name:
            if i in ani:
                print('it is a animal')
            elif i in bir:
                print('it is a bird')
            else:
                pass
        else:
            pass
else:
    print("name is not in data")



# --------------------------------------------



a = int(input("Enter Number: " ))
b= int(input("marks: "))
dict1 = [{'a':a,'b':b}]
for i in range(5):
    a = int(input("Enter Number: " ))
    b= int(input("marks: "))

    dict1.append({'a':a,'b':b})
    
print(dict1)