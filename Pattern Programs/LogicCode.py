
dict1 = {'s1':[100, 'available'],
        's2':[100, 'available'],
        's3':[100, 'available'],
        's4':[200, 'available'],
        's5':[200, 'available'],
        's6':[200, 'available'],
        's7':[300, 'available'],
        's8':[300, 'available'],
        's9':[300, 'available'] }       


a = int(input("Press 1 to start process:: "))
while a == 1:    
    book = input('Please Enter seat number you want to book:: ')
    if book in dict1.keys():
        for i,j in dict1.items():
            if i == book:
                if 'available' in j:
                    print('Your seat',book,'is booked...')
                    print('You have to Pay', j[0])
                    dict1[i][1] = 'unavailable'
                    # print(">>>>>>>>>>>>",dict1[i])
                    list1 = []
                    for x,y in dict1.items():            
                        if 'unavailable' in y:
                            if y[1] == 'unavailable':
                                list1.append(x)
                    print("Yours seats are:: ",list1)
                                               
                    a = int(input("Enter 1 for next booking, 2 for cancel your seat,3 for End process::"))

                    while a == 2:                           
                        cancel = input("Enter Seat number to cancel it::")
                        if cancel in list1:
                            # while len(list1):
                            dict1[cancel][1] = 'available'
                            print("Your seat is canceled..!!")
                            list1.remove(cancel)
                            print('Your avalible Seats are::',list1)
                            # break
                            a = int(input("Enter 1 Number for next booking, 2 for cancel anuthor seat, 3 for End Process:: "))
                        else:
                            print("This is not your seat !!! Please select your seat to cancel.")
                            a = int(input("Enter 1 for next booking, 2 for cancel your seat,3 for End process::"))                        
                else:
                    print("This seat is booked !!! please choose other seat::")
    else:
        print("Please Enter right Seat number::")
       
