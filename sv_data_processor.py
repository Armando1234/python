from os.path import isfile

accepted_filetypes = {
    "csv": ",",
    "tsv": "\t"
}

def open_separated_value_file(filename):

    if not isfile(filename):
        raise FileNotFoundError
    
    filetype = filename.rpartition(".")[2]

    if not filetype in accepted_filetypes:
        #Raise causes an error
        raise NotImplementedError

    try:
        file = open(filename, "r", encoding = "utf-8")
    except:
        file = open(filename, "r")
    finally: 
        # TODO
        yield next(file)
        for line in file:
            yield line.strip().split(accepted_filetypes[filetype])

def pipe_separated_values(pipeline, values):
    for pipe in pipeline:
        for processor, item in zip(pipe, next(values)):
            yield processor(item)

def apply_namedtuple(named_tuple, data):
    return named_tuple(*data)



# Testing code

if __name__ == "__main__":
    opened_file = open_separated_value_file("data_person_100000.csv")

    from collections import namedtuple
    from pprint import pprint

    Person = namedtuple("Person", next(opened_file))
    #print(dir(Person))

    piped_values = pipe_separated_values([[
        str,
        str,
        float,
        int,
        str
    ]], opened_file)

    #map applies function once to everything in a list of data/generator
    map(lambda person: apply_namedtuple(Person,data), piped_values)        


