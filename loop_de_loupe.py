# # For Loops
#
# # range(start, end, step)
# # End value is not included in the list!
#
# for i in range(1, 11):  # A sequence of 1 to 10
#     if i % 2 == 0:
#         print(i, " is even")
#     else:
#         print(i, " is odd")
#
# # Using the step iterator
#
# for i in range(1, 11, 3):  # A sequence from 1 to 10 with a step of 3
#     print(i)
#
# # Can use indicies to loop through a string
#
# float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
# print(float_list)
#
# for i in range(0, len(float_list)):  # Traverses the length of the arr
#     float_list[i] = float_list[i] * 2  # Replacing each item w/ its double
#
# print(float_list)
#
# # Can also loop through iterator directly
# float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
# count_greater = 0
#
# for num in float_list:  # Iterator traverses to the last index of the list
#     if num > 10:
#         count_greater += 1
#
# print(count_greater)

# Nested loops. The inner will always complete before the outer.
# n = 50
# num_list = [10, 4, 23, 6, 18, 27, 47]
# found = False
#
# for n1 in num_list:
#     for n2 in num_list:
#         if n1 + n2 == n:
#             found = True
#             break  # stop the inner loop
#     if found:
#         print(n1, n2)  # print the pair
#         break  # stop the outerloop
#
#
# #Continue keyword
# num_list = list(range(0, 10))
#
# for num in num_list:
#     if num == 3 or num == 6 or num == 8:
#         continue
#     print(num)
#

# Pass allows you to pass over code you need to write later
# num_list = list(range(20))
#
# for num in num_list:
#     pass # You can write code here later on
#
# print(len(num_list))

# While Loop
#Computing power before number hits 1000
n = 2
power = 0
val = n


while val < 1000:
    power += 1
    val *= n
print(power)


#Computing first and last digits of integer
n = 249
last = n % 10  # Finding the last number is easy

first = n  # Set it to `n` initially
while first >= 10:
    first //= 10  # Keep dividing by 10 until the leftmost digit is reached.

result = first + last
print(result)

