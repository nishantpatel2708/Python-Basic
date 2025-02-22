#tuple datatype
tup = ('fg', 67, True, 456.23, 'name')
print(tup)
print(type(tup))

change = list(tup)
print(type(change))
print(change)

change.append(False)

# change[0] = 'first'
print(change)

tup = tuple(change)
print(tup)



