# f = open("FileHandling\\A.txt", 'x')    ## CreateFile
# try:
#     f = open("FileHandling\\A.txt", 'r')

#     # f.write("Hello World!\n NISHANT")
#     # print(f.read(30))
#     print(f.readlines())
# except Exception as e:
#     print(e)

# else:
#     f.close()
#     print('File Closed')


## Copy Data

# try:
#     with open("FileHandling\\A.txt") as f1:
#         with open("FileHandling\\B.txt", "w") as f2:
#             for i in f1:
#                 f2.write(i)
# except Exception as e:
#     print('Error', e)


##Delete File
import os

if os.path.exists("FileHandling\\B.txt"):
    os.remove("FileHandling\\B.txt")
else:
    print('File is not found')
