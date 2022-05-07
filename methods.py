# Find method
# substring is what we're looking for, start and end define limits if needed
# a_string.find(substring, start, end)
# Replace method
# a_string.replace(substring_to_be_replaced, new_string)
# Letter case change
# string.upper(), string.lower()
# Join method
# string.join()
# Format string
# string1 = "This is a {version} of what {person} said".format(version="thing", person="Bob")

# Lamdas
# landa params:expression
# Commonly assigned directly to variables, kind of like an ES6 arrow function but easier
# Must be single line! Almost like a ternary operator...
tripleNum = lambda num: num * 3

print(tripleNum(33))

# Can work with multiple vars
concat_strings = lambda a, b, c: a[0] + b[0] + c[0]

print(concat_strings("World", "Wide", "Group"))


#  Can use conditionals but cannot drop the else. Else-wise, you'll get an error logged
my_func = lambda num: "High" if num > 50 else "Low"

print(my_func(30))

# Lambdas are better suited in function arguments

