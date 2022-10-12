#For seat
[s1,s2,s3] = 100,100,100
[s4,s5,s6] = 200,200,200
[s7,s8,s9] = 300,300,300

print (s1)
s1 = int(input("Enter number"))
print(s1)
book = int(input('Select Seat no'))
if book == 1 or 2 or 3:
    print('Your seat is booked.Your seat no. is {}.',book)
    # s = True
elif book == 4 or 5 or 6:
    print('Your seat is booked.Your seat no. is {}.',book)
    # B2[book-1] = True
elif book == 7 or 8 or 9:
    print('Your seat is booked.Your seat no. is {}.',book)
    # B3[book-1] = True1