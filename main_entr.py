# Code execution Timer
# Created by Armando Martinez
# 21/08/2019
# Method 1
#imports library "datetime"

from datetime import datetime
from sys import argv
from importlib import import_module
print(argv)


#while True:
#print(datetime.datetime.now())
    

#not infinite, but very long loop
#while True:

#if datetime.timedelta(datetime.datetime.now(), start_time) > 1000:
#sys.exit()
# #else:
# #continue

moduletotest = argv[2].strip(".py")


 
print("Module to test:\"" + moduletotest + "\"." )

start_time = datetime.now()
print("start at" + str(start_time))

#import moduletotest #imports "moduletotest.py" (as a "python file")
imported = import_module(moduletotest) # will import file specified in the variable


if hasattr(imported, "main"):
    imported.main()
else:
    print("The specified file has no entry method named \"main\"")

end_time = datetime.datetime.now()

time_taken =  end_time - start_time
print("operation took" + str(time_taken) + "to complete")


#if __name__ = "__main__"
#function with this name that will control all the code
#run our code