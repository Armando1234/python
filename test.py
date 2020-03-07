from sys import getsizeof

# Generators provide data one item at a time

#naive function - technical name
def stupidfunction():
    pies = []

    for _ in range(10000000):
        pies.append("3.141592")
    
    return pies

#lazy function - technical name
def smartfunction():

    for _ in range(10000000):
        yield "3.141592"


pies = smartfunction()
converted = map(float,pies)

print("Sum : {}".format(sum(converted)))
print("Size : {}".format(getsizeof(converted)))