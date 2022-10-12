# print("HEllo")
# print("HEllo")
# print("HEllo")
# print("HEllo")
# print("HEllo")
# print("HEllo")
# print("HEllo")
# print("HEllo")
# print("HEllo")
# print("HEllo")
#while
#for loop
# i=0
# while i<=10:
#     print("HEllo Loops",i)
#     # i=i+1
#     i+=1

# total=0
# i=1
# while i<=10:
#     # total+=i 
#     total=total+i
#     i=i+1
# print(total)

# n=int(input("enter num : "))
# n=(n*(n+1))/2
# print(n)


# i=0
# while True:
#     print(i)
#for loop
# for i in range(1,11,2):
#     print("hello",i)
# total=0
# for i in range(1,11):
#     total=total+i
# print(total)

# x = input("Enter your name : ")
# y = int(input("Enter your age : "))
# z = int(input("Enter your salary : "))

# if y > 18:
#     if z>25000:
#         print(x,"will pay income tax")
#     else:
#         print(x,"won't pay income tax")
# else:
#     print(x, ",You're a kiddo now")


# x = int(input("Enter a number : "))
# i=0
# while i<15:
#     x=i+1
#     print(x)


# Exercise 1
# total=0
# i=1
# x = int(input("Enter a number : "))
# while i<=x:
#     total+=i 
#     i=i+1
# print(total)


# Exercise 2
# x = 135
# y=0
# for i in str(x):
#     y += int(i)
# print(y)


# Exercise 3
# x = "My name is Vinod Rathod"
# y = {}
  
# for i in x:
#     if i in y:
#         y[i] += 1
#     else:
#         y[i] = 1
# print(y)

# name="chirag Joshi"
# name1=""

# for i in name:
#     if i not in name1:
#        name1+=i+" : "+str(name.count(i))
# print(name1)

# name="chirag"
# i=0
# while i<len(name):
#     print(name[i])
#     i+=1

# for i in range(1,6):
#     for j in range(1,i+1):
#      print("*",end="")
#     print("\n")


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print("\n")
    

# for i in range(5,0,-1):
#     for j in range(i+1,6):
#         print("* ",end="")
#     print("\n")


# increasing triangle pattern
# for i in range(5):
#     for j in range(i):
#         print('* ',end='')
#     print()

# decreasing triangle pattern
# for i in range(5):
#     for j in range(i,5):
#         print(chr(65+i),end='')
#     print()
# for i in range(4):
#     for j in range(1,i+3):
#         print(chr(65+i),end='')
#     print()

# print(chr(97))


# for i in range(5):
#     for j in range(i,5):
#         print('*',end=' ')
#     for j in range(i+1):
#         print('#',end=' ')
#     for j in range(i+1):
#         print('$',end=' ')
#     print()


# n = int(input("Row: "))
# for i in range(n):
#     for j in range(0,n-1):
#         print(end=' ')
#     n=n-1
#     for j in range(i+1):
#         print("*",end=' ')
#     print()

# print()

# for i in range(n):
#     for j in range(n-i):
#         print("*",end=' ')
#     print()

# print()


# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=' ')
#     for j in range(i+1):
#         print("*",end=' ')
#     print()

# print()


# for i in range(n):
#     for j in range(i+1):
#         print(chr(65),end=' ')
#     print()
