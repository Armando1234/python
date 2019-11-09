from datetime import datetime
from random import randint


numbers = []
for i in range (5):

    name = str(randint(2000,3000))
    age = randint(1, 30)
    birthday = randint(1,28)
    birthmonth = randint(1,12)
    birthyear = (datetime.now().year - age) #% 100 (Modulus to only display last two digits)
    print("my name is {}, and I am {} years old. My birthdate is {:02}/{:02}/{}".format(name,age,birthday,birthmonth,birthyear))
    #print(f"my name is {name}, and I am {age} years old. My birthdate is {birthday:02}/{birthmonth:02}/{birthyear}")
    numbers.append(birthyear)
print(numbers)
