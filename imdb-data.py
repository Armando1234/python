from statistics import mean, median, mode


def reader(filename):
    #with closes the file for us: closing files is very important after they have been opened and accessed
    file = open(filename, "r", encoding = "utf-8")
        #UTF recognizes every character on earth
    for row in file:
        yield row

    


def main():
    #create generator, save in __data__ variable
    data = reader("data.tsv")

    genres = {}
        
    #next function kicks generator to skip first item             O_   ______      
    #                                                            /|__ *|next|
    #                                                            /    *|/VV\|

    #                                               O__ _______
    #                                              /|   |Yield|
    #                                              / \  |/VVV\|  
    # yield function- loops through everything once without restarting function

    next(data)

    #loops through yielded items one at a time
    for row in data:
        items = row.split("\t")
            #\t = tab
        if len(items) == 9:
            genre_string = items[8]
            for genre in genre_string.split(","):
                if genre in genres.keys():
                    genres[genre] +=1
                else:
                    genres[genre] = 1

    with open("imdb-data-results.txt","w") as file:
        print(genres)

main()