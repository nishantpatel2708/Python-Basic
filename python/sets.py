#sets intro
# set is nothing but set is just datatype 

# unorder collection of unique data  
# s={1,3,4,5,3}
# print(s)
# duplicate value not count you  can add the duplicate then after it return single time  

# you can not use indexing[0]

#set function
# l=[1,2,3,4,5,6,7,4,5,6,7,3,5]
# temp=[]
# for i in l:
#     if i not in temp:
#         temp.append(i)
# print(temp)
# s1=set(l)
# temp=list(s1)
# print(temp)
# s={1,4,3,5,6,7}
# # set method
# # ad the dat in set
# s.add(10)
# #remove method in  set
# s.remove(4)
# s.remove(10)#error
# #discard method
# s.discard(5)
# print(s)
# s.clear()
# scpy=s.copy()
# store in sets 
#  not store list tuple dict
# store only num str float 
# name={'chirag','joshi'}
# #in keyword in set
# if 'chirag' in name:
#     print(True)
# else:
#     print(False)
# # for loop in set 
# for i in name:
#     print(i)
# print(name)
# set in math 
s1={1,2,3,4}
s2={3,4,5,6}
print(s1|s2)
print(s1&s2)
# print(s)
