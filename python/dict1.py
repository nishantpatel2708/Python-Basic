# dictname={'key':'value'}

#dict no support indexing

# user={'name':'Chirag','age':54}
# user1=dict(name='Chirag')
# print(user1)

# which datatype you store in dict
# num
# float
# string
# list
# tuple

user_info={
    'name':"Chirag",
    'age':58,
    'height':5.6,
    'fav_movie':['DDLG','COCO'],
    'fav_song':('DIL',"REER"),
} 

#add the data in  dict
user_info['width']=5.8
print(user_info)

#in keyword
#check key
if 'name' in user_info:
    print('YES')
else:
    print("no")

#check values
# if 'Chirag' in user_info.values():
#     print('YES')
# else:
#     print("no")

# looping in dict 

# for i in user_info:
#     print(i)

# for i in user_info.values():
#     print(i)

# user_info_keys=user_info.keys()
# print(user_info_keys)
# user_info_value=user_info.values()
# print(user_info_value)
for i in user_info:
    print(user_info[i])
# user_info_item=user_info.items()
# print(user_info_item)

# for key,value in user_info.items():
#     print(f"your dict key is {key} and its value is {value}")

#dict len
# print(len(user_info))

#remove method in dict
#pop
# user_info.pop('name')
# user_info.popitem()
# del user_info['name']

#copy method
# user_info_copy=user_info.copy()
# print(user_info_copy)
# user_info.clear()
# print(user_info)