# Write a program that takes a string as input and returns a new string that contains the same letters as the input string, but in alphabetical order.
# Example usage:

# input_str = "hello, world!"

# Output:
#  !,dehllloorw

var1 = input("Enter string: ")
arr = []

for i in var1:
    arr.append(i)

arr.sort()
new_string = ''

for j in arr:
    new_string += j

print(new_string)