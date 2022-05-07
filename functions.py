# Min method
minimum = min(10, 40)
print(minimum)

minimum = min(10, 100, 1, 1000)  # It even works with multiple arguments
print(minimum)

minimum = min("Superman", "Batman")  # And with different data types
print(minimum)


# Blocks are determined by indentation not brackets! Two returns after blocks is standard

def my_function():
    print("This is awesome!")


my_function()


def minimum(first, second):
    if first < second:
        return first
    else:
        return second


num1 = 100
num2 = 40

result = minimum(num1, num2)

print(result)
