# Write a program that takes a list of integers as input and returns the longest consecutive subsequence of consecutive integers within that list.

# For example, given the input list [1, 3, 4, 5, 7, 8, 9, 11, 13], the program should return the subsequence [3, 4, 5], since this is the longest consecutive subsequence of consecutive integers within the list.

# Example usage:
numbers = [1, 3, 4, 5, 7, 8, 9, 11, 13]
# longest_subsequence = longest_consecutive_subsequence(numbers)
# print(longest_subsequence)


# def fun1(numbers):
#     arr1 = []
#     consecutive = []
#     var = 0
#     for i in numbers:
#         var = i
#         print(i , var )
#         if i == var :
#             arr1.append(i)
#         else:
#             consecutive.append(arr1)
#             arr1 = []
#             var = i
#     print(arr1)
#         # arr1.append(i)
#         # if i == arr1[-1]:
#         #     print(arr1)
#         #     consecutive.append(arr1)
#         # else:
#         #     arr1 = []

# fun1(numbers)


def longest_consecutive_subsequence(numbers):
    numbers_set = set(numbers)
    longest_subsequence = []
    current_subsequence = []

    for num in numbers:
        if num - 1 not in numbers_set:
            current_subsequence = [num]

            while num + 1 in numbers_set:
                num += 1
                current_subsequence.append(num)

            if len(current_subsequence) > len(longest_subsequence):
                longest_subsequence = current_subsequence

    return longest_subsequence

numbers = [1, 3, 4, 5, 7, 8, 9, 11, 13]
longest_subsequence = longest_consecutive_subsequence(numbers)
print(longest_subsequence)