from statistics import mean, median, mode


def reader(filename):
    #with closes the file for us: closing files is very important after they have been opened and accessed
    with open(filename, "r", encoding = "utf-8") as file:
        #UTF recognizes every character on earth
        data = file.read()
        return data
    


def mainapp():
    data = reader("app-store.csv").splitlines()

    ratings = []
    for row in data[1:]:
        items = row.split(",")
        #splits rows on comma
        try:
            value = float(items[6])
            if value <= 5:
                ratings.append(value)
        except ValueError:
            pass


    print("App Store Max : {}".format(max(ratings)))
    print("App Store Min : {}".format(min(ratings)))
    print("App Store Mean : {}".format(mean(ratings)))
    print("App Store Median : {}".format(median(ratings)))
    print("App Store Mode : {}".format(mode(ratings)))


    #print(type(data))
    #print(len(data))
def mainplay():
    data = reader("play-store.csv").splitlines()

    ratings = []
    for row in data[1:]:
        items = row.split(",")
        #splits rows on comma
        try:
            value = float(items[2])
            if value <= 5:
                ratings.append(value)
        except ValueError:
            pass


    print("Play Store Max : {}".format(max(ratings)))
    print("Play Store Min : {}".format(min(ratings)))
    print("Play Store Mean : {}".format(mean(ratings)))
    print("Play Store Median : {}".format(median(ratings)))
    print("Play Store Mode : {}".format(mode(ratings)))


    #print(type(data))
    #print(len(data))

mainapp()
mainplay()