# input = input("Input the  temperature you like to convert : ")
# temp = (input[:-1])
# unit = input[-1] 

# def convert(temp, unit):
#     unit = unit.lower()
#     if unit == "c" and temp != "":
#         temp = 9.0 / 5.0 * int(temp) + 32
#         return temp
    
#     elif unit == "f" and temp != "":
#         temp = (int(temp) - 32)  / 9.0 * 5.0
#         return temp
#     else:
#         r = "Wrong input"
#         return r
# print(convert(temp, unit))



# ---------------------------------------------------



# id = int(input("Enter ID Number:"))
# name = input("Enter Name:")
# marks = float(input("Enter Your marks:"))
# data = [{'id' : id, 'name' : name, 'marks' : marks}]

# if marks <= 100:
#     a = int(input("Enter 1 to add data or 2 to show data:"))
#     while a == 1:
#         id = int(input("Enter ID Number:"))
#         name = input("Enter Name:")
#         marks = float(input("Enter Your marks:"))
#         if marks <= 100:
#             data.append({'id' : id, 'name' : name, 'marks' : marks})
#             a = int(input("Enter 1 to add data or 2 to show data:"))
            
#         else:
#             print("Enter marks between 100")
#             break    
#     else:
#         print(data)
# else:
#     print("Enter marks between 100")



# ---------------------------------------------------


# # ------Fibonacci triangle
 
# def fiboTriangle(n):
 
    
#     f=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#     # f=[1,4,9,16,25,36,49,64,91,100]
 
#     fiboNum = 0
 
#     for i in range(1, n + 1):
#         for space in range(1, (n-i)+1):
#             print(' ',end=" ")
#         for j in range(1, i + 1):
 
#             print(f[fiboNum], " ", end="")
#             fiboNum = fiboNum + 1
 
#         print()

# n = 4
# fiboTriangle(n)


# ---------------------------------------------------



# row_size = 4
# # row_size = int(input("Enter the row size: "))
# a = 0
# b = 1
# c = a+b
# for i in range(1, row_size+1):
#     for j in range(1, (row_size-i)+1):
#         print(end=" ")
#     for inn in range(1, i+1):
#         print(c, end=" ")

#         c = a+b
#         a = b
#         b = c
#     print("")



# ---------------------------------------------------



# row_size = 3
# a = 0
# b = 1
# c = a+b
# t=1
# for i in range(1, row_size+1):
#     for j in range(1, (row_size-i)+1):
#         print(end=" ")
#     for inn in range(1, i+1):
#       if t==1:
#         print(a, end=" ")
#         t = t+1
#       else:
#         print(c, end=" ")

#         c = a+b
#         a = b
#         b = c
#     print("")
# for i in range(row_size-1, 0, -1):
#     for j in range(row_size-i-1):
#         print(end=" ")
#     for j in range(0,i):
#         print(c, end=" ")
#         c = a+b
#         a = b
#         b = c
#     print("")




# ---------------------------------------------------




# import pandas as pd
# class State:

#     state_train = {"Bihar":[23500, 17237, 5927],
#             "Orissa":[22658, 24555, 2364]
#             }
#     def __init__(self):
#         return self.state_train

#     state_bus = {
#         "U.P": [36517, 22617, 6314],
#         "Jharkhand": [23254, 19845, 1336]
#     }
#     def __init__(self):
#         return self.state_bus


# class Transport(State):

#      def __init__(self, transport):
#         if transport == "Train" or transport == "train":
#             df = pd.DataFrame(self.state_bus).T
#             df.reset_index(inplace=True)
#             print("By Bus\n"  + "--------------- ")
#             df.columns = ['Destination state','Men','Women','Women']
#             print(df)

#         else:
#             df = pd.DataFrame(self.state_train).T
#             df.reset_index(inplace=True)
#             print("By Train\n"  + "--------------- ")
#             df.columns = ['Destination state','Men','Women','Women']
#             print(df)


# a = Transport("train")
# a = Transport("bus")


# n = 9
# a = 0
# b = 1
     
#     # Check is n is less
#     # than 0
# if n < 0:
#     print("Incorrect input")
        
# # Check is n is equal
# # to 0
# elif n == 0:
#     print (0)
    
# # Check if n is equal to 1
# elif n == 1:
#     print (b)
# else:
#     for i in range(1, n):
#         c = a + b
#         a = b
#         b = c
#         print(b)
    
# Driver Program



# ---------------------------------------------------

# sort array using loop
# array = [1,2,3,4,5,6,7,8,9,10]

# new_array = []

# while array:
#     min = array[0]
#     for x in array:
#         if x > min:
#             min = x
#     new_array.append(min)
#     array.remove(min)
# print(new_array)