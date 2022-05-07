# def rec_count(number):
#     print(number)
#     # Base Case
#     if number == 0:
#         return 0
#     # Recursive call with a different argument
#     rec_count(number - 1)
#     print(number)
#
#
# rec_count(5)


# There needs to be a base case else the recursive function will crash! Much like a while loop

# running a fibonaci to return where it is in the sequence
def fib(n):
    if n <= 1:  # first number in sequence
        return 0
    elif n == 2:  # second number in sequence
        return 1
    else:
        #Recursive call
        return fib(n - 1) + fib(n - 2)


print(fib(6))