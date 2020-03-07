for i in range (10):
    
    for j in range (i):
        print("-", end="")
    print("X", end="")
        
    for j in range (9-i,0,-1):
        print("-", end="")

    print()


for i in range (10):
    for j in range (10):
        if i == j or i == (9-j):
            print("X", end="")
        else:
            print("-", end="")
    print()



    #prints a new line by default
    #end character allows for everything to be printed in one line - 
    #print statements print a character after the string. by default, this character is a new line, but it can be overridden with other prompts like "end"