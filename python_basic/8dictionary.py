dict1 = {'key1': 'value', 'key2': 'value2', 'key3': 100}

print(type(dict1))
print(len(dict1))

x = dict1['key3']
print(x)


dict1['key2'] = True
print(dict1)


print(dict1.keys())
print(dict1.values())




dict1.pop('key1')
print(dict1)

dict1.popitem()
print(dict1)


dict1 = {'key1': 'value', 'key2': 'value2', 'key3': 100}

dict1['key3'] = 456
print(dict1)

mydict = dict1.copy()
print(mydict)

del mydict
# print(mydict)

dict1.clear()
print(dict1)