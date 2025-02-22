# a = [7,4,2]
# # sum =sum(a)
# # print(sum)
# z = []
# # p = a[1:]
# # print(p)
# # for i in p:
# #     print(i)
# #     z.append(i)
# # print(z)
# if a != z:
#     for i in a:
#         z.append(i)
#     print("z: ",z)
#     sum = sum(z)
#     print(sum)
#     z.clear()
#     k=a[1:]
#     for i in k:
#         z.append(i)
#     print(z)    
#     e = sum(z)
#     print(e)
    # sum = sum + sum    
    # z.append(a[1:])
    # for i in len(z):
    #     print(i)
    # q = sum(s)
    # sum = sum(s) + sum



    # for i in z:
    #     b = sum(a[1:]) + z
    # print(b)

# set1 = {}

# dict1 = {'s1':[100, 'available'],'s2':[100, 'unavailable'],'s3':[100, 'unavailable'],'s4':[200, 'available'],'s5':[200, 'available'],'s6':[200, 'available'],'s7':[300, 'available'], 's8':[300, 'available'],'s9':[300, 'available'] }
# for x,y in dict1.items():
#     if 'unavailable' in y:
#         if y[1] == 'unavailable':
#             set1[x] = y
# print(set1)
            # break
# print(y)

        # print(booked)
        # break



        


dict1 = {'s1':[100, 'available'],
        's2':[100, 'available'],
        's3':[100, 'available'],
        's4':[200, 'available'],
        's5':[200, 'available'],
        's6':[200, 'available'],
        's7':[300, 'available'],
        's8':[300, 'available'],
        's9':[300, 'available'] }       

Stock = [{'CE': 12233, 'strikeprice' : 41000, 'PE': 35521},
{'CE': 12233, 'strikeprice' : 41000, 'PE': 35521},
{'CE': 12233, 'strikeprice' : 41000, 'PE': 35521},
{'CE': 12233, 'strikeprice' : 41000, 'PE': 111},
{'CE': 12233, 'strikeprice' : 41000, 'PE': 35521},
{'CE': 12233, 'strikeprice' : 41000, 'PE': 35521},]
PE = 111
# a = int(input("Press 1 to start process:: "))
list1= []
for i in Stock:
    for j,k in i.items():
        if k == PE:
            print(i)
            for z,x in i.items():
                list1.append(x)
            g = list1[1]
            sum = g + 90
            print(sum)
            
            
        











 




