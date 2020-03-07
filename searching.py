
def main():
    with open("numbers.txt", "r") as file:
    
        #map applies a function to all items in a for loop
        numbers = list(map(int,file.read().splitlines()))
    
    print(type(numbers))
    print(len(numbers))
    print(type(numbers[0]))

    linear_result = linear_search(numbers, 6666666)
    binary_result = binary_search(numbers, 6666666)
    print("(linear search) Position of Needle: {}".format(linear_result))
    print("(linear search) Number at position: {} was {}".format(linear_result, numbers[linear_result]))
    print("(binary search) Position of Needle: {}".format(binary_result))
    print("(binary search) Number at position: {} was {}".format(binary_result, sorted(numbers)[binary_result]))

#needle - "needle in a hay stack" (thing we are looking for)
def linear_search(data, needle):    
    #enumerate makes the for have 2 variables, one is the value of the item in the (index) position in the list and the other is the index
    for index, num in enumerate(data):
        if num == needle:
            # return position of the item
            
            return index 





def binary_search(data, needle):
    sorted_data = sorted(data)
    left_index = 0
    right_index = len(sorted_data)

    #converting to int rounds down
    while True:
        middle_index = int((right_index - left_index) / 2 + left_index) 
        print("looking at {} between {} and {}".format(middle_index, left_index, right_index))

        num = sorted_data[middle_index]
        
        if num > needle:
            right_index = middle_index
        elif num < needle:
            left_index = middle_index
        else:
            return middle_index 
    


main()
