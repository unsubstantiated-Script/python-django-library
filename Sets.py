# One might wonder, “Why would I need a set?”
# Well, a set is perfect when we simply need to keep track of the existence of items.
# It doesn’t allow duplicates, which means that we can convert another data structure to a set to remove any duplicates.

# random_set = {"Educative", 1408, 3.142,
#               (True, False)}
# print(random_set)
# print(len(random_set))  # Length of the set

# Set() constructor allowing us to make empty sets
# empty_set = set()
# print(empty_set)
#
# random_set = set({"Educative", 1408, 3.142, (True, False)})
# print(random_set)

# To add a single item, we can use the add() method. To add multiple items, we’d have to use update().
# The input for update() must be another set, list, tuple, or string.
# empty_set = set()
# print(empty_set)
#
# empty_set.add(1)
# print(empty_set)
#
# empty_set.update([2, 3, 4, 5, 6])
# print(empty_set)

# Deleting Elements #
# The discard() or remove() operations can be used to delete a particular item from a set:
# random_set = set({"Educative", 1408, 3.142, (True, False)})
# print(random_set)
#
# random_set.discard(1408)
# print(random_set)
#
# random_set.remove((True, False))
# print(random_set)


# The for loop can be used on unordered data structures like sets.
# However, we wouldn’t know the order in which the iterator moves meaning elements will be picked randomly.
# odd_list = [1, 3, 5, 7]
# unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}
#
# print(unordered_set)
#
# for num in unordered_set:
#     if (not num % 2 == 0):
#         odd_list.append(num)
#
# print(odd_list)

# Sets are not ordered, and they can change as the software sees fit for storage
# If we want them ordered, we need to impose the above to reorder them into a list.
# Set theory operations
# Folks familiar with mathematics will know that sets have three main operations:
# union, intersection, and difference.

# Union
# Collection of all unique elements from both sets
# In Python, union can be performed using either the pipe operator, |, or the union() method:
# set_A = {1, 2, 3, 4}
# set_B = {'a', 'b', 'c', 'd'}
#
# print(set_A | set_B)
# print(set_A.union(set_B))
# print(set_B.union(set_A))


# Intersection
# Where two sets share common items only
# set_A = {1, 2, 3, 4}
# set_B = {2, 8, 4, 16}
#
# print(set_A & set_B)
# print(set_A.intersection(set_B))
# print(set_B.intersection(set_A))

# Difference
# All Unique items only present in the first set vs. the second
# set_A = {1, 2, 3, 4}
# set_B = {2, 8, 4, 16}
#
#
# print(set_A - set_B)
# print(set_A.difference(set_B))
#
# print(set_B - set_A)
# print(set_B.difference(set_A))
