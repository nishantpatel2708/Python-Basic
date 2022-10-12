# file oparation
# f=open('1sr.txt')
# print(f.read())
# print(f.read())
#tell mane khabar padse ktya che maru cursor
# print(f"cursor postion is - {f.tell()}")
#Fseek cursor cghange karva mate
# f.seek(0)
# f.seek(5)

# print(f"cursor postion is - {f.tell()}")
# print(f.read())
#
# print(f.readline())Ek line ne read karva mate
# print(f.readlines())vbadhi lone nu list return karse...
# print(f.closed)#file close thai che ke nai check karva mate

# f.close()
# print(f.closed)
# with block
# with open('1sr.txt') as f:
#     data=f.read()
#     print(data)
#write file
# with open('1sr.txt','w') as f:
#     f.write('hello chirag')
# append file 
# with open('3sr.txt','a') as f:
#     f.write('\nhello mitul\n')
with open('1sthtml.html','w') as f:
    f.write('''
    <!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Background image</title>

</head>
<body style="color:yellow;">
	
	<div style="background-image: url('batman_12-wallpaper-1920x1080.jpg');">
		<p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p>
		<p> Background image</p>
		<p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p><p> Background image</p>
	</div>
</body>
</html>''')
