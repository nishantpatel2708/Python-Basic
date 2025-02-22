# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))


# num = 100
# print("The factorial of", num, "is", factorial(num))



# def max_treasure(treasure_map):
#     if not treasure_map:
#         return 0

#     for row in treasure_map:
#         for item in row:
#             if item < 0:
#                 return -1

#     def dfs(i, j):
#         if i < 0 or i >= len(treasure_map) or j < 0 or j >= len(treasure_map[0]) or treasure_map[i][j] == 0:
#             if i >= len(treasure_map):
#                 print(i , len(treasure_map))
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
#                 [0, 1, 4, 0, 0],
#                 [5, 0, 0, 3, 0]]
# print(max_treasure(treasure_map))


def max_treasure(treasure_map):
    if not treasure_map:
        return 0

    rows = len(treasure_map)
    cols = len(treasure_map[0])

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or treasure_map[i][j] == 0:
            return 0

        treasure = treasure_map[i][j]
        treasure_map[i][j] = 0

        up = dfs(i - 1, j)
        down = dfs(i + 1, j)
        left = dfs(i, j - 1)
        right = dfs(i, j + 1)

        treasure_map[i][j] = treasure

        return max(up, down, left, right) + treasure

    max_treasure = 0
    for i in range(rows):
        for j in range(cols):
            if treasure_map[i][j] != 0:
                max_treasure = max(max_treasure, dfs(i, j))

    return max_treasure if max_treasure > 0 else -1
treasure_map = [[3, 0, 0, 1, 2],
                [0, 1, 4, 0, 0],
                [5, 0, 0, 3, 0]]
print(max_treasure(treasure_map))