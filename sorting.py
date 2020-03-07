
from random import randint

#long way

#data = []
#for i in range (10000):
#    data[i] = randint(0, 10000)

#short way, can be optimized
#data = [randint(0, 10000) for _ in range (100)]


#the underscore can be used as an "empty" or "unused" variable to replace the "i" which would not be needed
data = [1,2,3,4,5]

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




#an algorith is a repeatable series of steps

#stupid algorithms:


def shuffle_sort(data):
    while not sorted(data) == data:
        data.shuffle()
    return data

def miracle_sort(data):
    while not sorted(data) == data:
        time.sleep(10)
    return data




#the __name__ of a python file is only ever "__main__" when the file is run directly. otherwise it's filled with nonsense.

if __name__ == "__main__":
    print("Running bubble sort")
    bubble()





