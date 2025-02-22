# # Python Program to Count Vowels and Consonants in a String

# str1 = input("Please Enter Your Own String : ")
# vowels = 0
# consonants = 0
# # str1.lower()

# for i in str1:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
#        or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#         vowels = vowels + 1
#     else:
#         consonants = consonants + 1
 
# print("Total Number of Vowels in this String = ", vowels)
# print("Total Number of Consonants in this String = ", consonants)



# # Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1





# # Function for nth Fibonacci number
# def Fibonacci(n):
   
#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")
 
#     # Check if n is 0
#     # then it will return 0
#     elif n == 0:
#         return 0
 
#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
 
# # Driver Program
# print(Fibonacci(6))




# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fib(10)


# Define the 2D map array with numbers representing treasures
# map_2d_array = [[3, 0, 0, 1, 2],
# [0, 1, 4, 0, 0],
# [5, 0, 0, 3, 3]]

# # Function to get treasures and terrain for a specific cell
# def get_cell_info(row, col):
#     treasures = map_2d_array[row][col]
#     return f"In this location, you find {treasures} treasure(s)."

# # Function to get total treasures in the whole map
# def get_total_treasures():
#     total_treasures = 0
#     for row in map_2d_array:
#         total_treasures += sum(row)
#     return f"Total treasures in the entire map: {total_treasures}"

# # Example usage
# print(get_cell_info(3, 3))  # Output: "In this location, you find 4 treasure(s)."
# print(get_total_treasures())  # Output: "Total treasures in the entire map: 13"

# def max_treasure(treasure_map):
#     def is_valid_move(x, y):
#         return 0 <= x < rows and 0 <= y < cols and treasure_map[x][y] != 0

#     def dfs(x, y):
#         if not is_valid_move(x, y):
#             return 0
#         current_treasure = treasure_map[x][y]
#         treasure_map[x][y] = 0  # Mark the city as visited
#         max_collected = 0
#         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             new_x, new_y = x + dx, y + dy
#             max_collected = max(max_collected, dfs(new_x, new_y))
#         treasure_map[x][y] = current_treasure  # Restore the city's treasure value
#         return max_collected + current_treasure

#     rows = len(treasure_map)
#     cols = len(treasure_map[0])
#     max_collected = 0

#     for i in range(rows):
#         for j in range(cols):
#             if treasure_map[i][j] == 0:
#                 continue
#             max_collected = max(max_collected, dfs(i, j))

#     return max_collected

# # Example usage
# treasure_map1 = [
#     [3, 0, 0, 1, 2],
#     [0, 1, 4, 0, 0],
#     [5, 0, 0, 3, 3]
# ]

# treasure_map2 = [
#     [3, 0, 0, 1, 2],
#     [0, 1, 4, 0, 0],
#     [5, 0, 0, 3, 0]
# ]

# print(max_treasure(treasure_map1))  # Output: 6
# print(max_treasure(treasure_map2))  # Output: 5

# def max_treasure(treasure_map):
#     if not treasure_map:
#         return 0

#     for row in treasure_map:
#         for item in row:
#             if item < 0:
#                 return -1

#     def dfs(i, j):
#         if i < 0 or i >= len(treasure_map) or j < 0 or j >= len(treasure_map[0]) or treasure_map[i][j] == 0:
#             return 0

#         treasure = treasure_map[i][j]
#         treasure_map[i][j] = 0

#         up = dfs(i - 1, j)
#         down = dfs(i + 1, j)
#         left = dfs(i, j - 1)
#         right = dfs(i, j + 1)

#         treasure_map[i][j] = treasure

#         return max(up, down, left, right) + treasure

#     max_treasure = 0
#     for i in range(len(treasure_map)):
#         for j in range(len(treasure_map[0])):
#             if treasure_map[i][j] != 0:
#                 max_treasure = max(max_treasure, dfs(i, j))

#     return max_treasure


# treasure_map = [[3, 0, 0, 1, 2],
# [0, 1, 4, 0, 0],
# [5, 0, 0, 3, 0]]
# print(max_treasure(treasure_map))




# Using a Python dictionary to act as an adjacency list
# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }

# visited = set() # Set to keep track of visited nodes of graph.

# def dfs(visited, graph, node):  #function for dfs 
#     if node not in visited:
#         print (node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)

# # Driver Code
# print("Following is the Depth-First Search")
# dfs(visited, graph, '5')



import json

isRunning = True

def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def add_new_item(data):
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    new_item = {
        "id": len(data['items']) + 1,
        "name": item_name,
        "price": item_price
    }
    data['items'].append(new_item)
    print("Item added successfully!")

def take_order():
    pass

def take_command(data):
    print("Welcome to our bakery system \nPlease select a command:")
    print("1. Add a new item")

    command = int(input(""))
    if command == 1:
        add_new_item(data)

# Load initial data from file
data = load_data()

while isRunning:
    take_command(data)
    isRunning = False

# Save updated data back to file
save_data(data)

# Print updated JSON data
print(json.dumps(data, indent=4))
