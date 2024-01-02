
#program to print path variable in environment varialbes 

import os

variable= os.environ['path']
path_var=variable.split(";")
print(len(path_var))
for i in path_var :
    print(i)