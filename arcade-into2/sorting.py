
from random import randint

#long way

#data = []
#for i in range (10000):
#    data[i] = randint(0, 10000)

#short way, can be optimized
#data = [randint(0, 10000) for _ in range (100)]

data = [1,2,3,4,5]
#the underscore can be used as an "empty" or "unused" variable to replace the "i" which would not be needed


def bubble():
    operations = 0
    swaps = 0
    for i in range(len(data)):
        previousswaps = swaps
        for j in range(len(data) -i -1):
            operations += 1
            first = data[j]
            second = data[j+1]

            #print("comparing {} and {} ".format(first,second))


            if first > second:
                #print("swapping {} and {}".format(first, second))

                data[j] = second
                data[j+1] = first
                swaps += 1

        if previousswaps == swaps:
            break     

        

    print("Swapped {} times".format(swaps))
    print("Looped {} times".format(operations))


bubble()





