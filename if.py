price = 200

if price >= 300:
    price *= .3
elif 300 > price >= 200:
    price *= .2
elif 200 > price >= 100:
    price *= .1
elif 100 > price < 0:
    price *= .05

print(price)
