# # 1. Fibonacci series
# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fib(10)

# # 2. Factorial
# n = int(input("Num : "))
# fact = 1
  
# for i in range(1,n+1):
#     fact = fact * i
      
# print ("The factorial of", n ,"is : ",end="")
# print (fact)

# # 3. prime number
# n = int(input("Num : "))
# if n>1:
#     for i in range(2,n):
#         if (n % i) == 0:
#             print(n,"is not a prime number")
#             break
#     else:
#             print(n,"is a prime number")
# else:
#             print(n,"is not a prime number")

# # 4. pattern
# def patt():
#     for i in range(n):
#         for j in range(i):
#             print('*',end=' ')
#         print()
# n = int(input("Num : "))
# patt()

# # 5. reverse string
# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
    
# s = input("Your string is :")
# print ("The reversed string(using loops) is : ",end="")
# print (reverse(s))
  


# 6. table
# n =int(input("Num : "))
# for i in range(1,11):
#     print(n, "*", i, "=", n*i)



# 7. 
# list 
# l=[2,3,4,5,6,"Seven","Eight"]
# # print(l[3:5])
# # l[0]="Two"
# # l[2:]=["Chirag"]
# # l.append("nine")
# # print(l.index('Seven'))
# # print(type(l[5]))
# # print(l.insert(5,l[5].replace("S","H")))
# # l.insert(2,"Chirag")
# m=[5,2,7]
# l.extend(m)
# print(l[0]*m[0])
# print(l)

