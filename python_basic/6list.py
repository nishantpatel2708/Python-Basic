# Lists are created using square brackets:
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.  



list1 = ["name", 45, 56.2, True, 54]
print(list1)
# print(type(list1))
# print(len(list1))
# print(list1[0])


# new = list1[-1]
# print(new)

list1[0] = 90
print('Change value:',list1)

list1.insert(2, "54")
print('insert:',list1)

list1.append(False)
print('append:',list1)

list1.remove(56.2)
print('remove:',list1)

list1.pop(0)
print('pop:',list1)


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



