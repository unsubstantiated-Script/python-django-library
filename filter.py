# filter and map both return new objects that don't manipulate the original string
numList = [30, 2, -15, 17, 9, 100]

greater_than_10 = list(filter(lambda n:n > 10, numList))

print(greater_than_10)