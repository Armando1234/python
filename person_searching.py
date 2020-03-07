from collections import namedtuple

def main():
    with open("data_person_100000.csv", "r", encoding="utf-8") as file:
        people_strings = file.read().splitlines()

    Person = namedtuple("Person", people_strings[0])

    people = []
    for p in people_strings[1:]:
        
        #asterisk splits list in separate variables of the expected type
        person_data = p.split(",")
        people.append(Person(*person_data))

    print(people[0:5])




#first class functions:

def weirdfunction(function_to_run):
    function_to_run()
weirdfunction(main)
