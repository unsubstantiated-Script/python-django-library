# Only adds to end of list
# a_list.append(newElement)

# num_list = []
# num_list.append(1)
# num_list.append(2)
# num_list.append(3)
# num_list.append(4)
#
# print(num_list)

# Adds in anywhere you want?
# a_list.insert(index, newElement)

# num_list = [1, 2, 3, 5, 6]
# num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
# print(num_list)

# Pop removes from end
# houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
# last_house = houses.pop()
# print(last_house)
# print(houses)

# Slice for sublist
# num_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(num_list[2:5])
# print(num_list[0::2])

# #Finding indices
# cities = ["London", "Paris", "Los Angeles", "Beirut"]
# print(cities.index("Los Angeles"))  # It is at the 2nd index

# Verifying existence in the list
# cities = ["London", "Paris", "Los Angeles", "Beirut"]
# print("London" in cities)
# print("Moscow" not in cities)

# Sorting Lists
# num_list = [20, 40, 10, 50.4, 30, 100, 5]
# num_list.sort()
# print(num_list)

# List Comprehension like .map() or .forEach() in JS
# nums = [10, 20, 30, 40, 50]
# nums_double = []
#
# for n in nums:
#     nums_double.append(n * 2)
#
# print(nums)
# print(nums_double)

# Rewritten in list comprehension
# nums = [10, 20, 30, 40, 50]
#
# # List comprehension for each n, multiply by 2
# nums_double = [n * 2 for n in nums]
#
# print(nums)
# print(nums_double)

# # Throwing in a condition
# nums = [10, 20, 30, 40]
# # Only doubles if divisible by 4
# nums_double = [n * 2 for n in nums if n % 4 == 0]
#
# print(nums)
# print(nums_double)

# Using multiple lists
# list1 = [30, 50, 110, 40, 15, 75]
# list2 = [10, 60, 20, 50]
#
# sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]
#
# print(sum_list)
