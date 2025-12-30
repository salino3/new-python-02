import platform
import random  
import subprocess
from platform import python_implementation, python_version_tuple
import os
 

my_list = [1, 2, 3, -4.8, 5.9, 6, 7, 8, 9, 10, 3, 400, 5, 6, 7, 8, 9, 10]

# choose one element or a list of elements ramdomnly
print(random.choice(my_list))
print(random.choice([my_list]))
# print(random.choice([])) # Error
print(random.sample(my_list, 5))
print(random.sample(my_list, 1))
print(random.sample(my_list, 0))

  
print(platform.platform())
print(platform.platform(1))
print(platform.platform(0, 1)) 
print(platform.machine()) 
print(platform.version()) 
print(platform.processor())
print(platform.system())


cpu = platform.processor()
print(cpu)
result = subprocess.check_output("wmic cpu get name", shell=True)
print(result.decode())

if "Intel" in cpu:
    print("Es Intel")


print("------------------------")
 
print(python_implementation())

for atr in python_version_tuple():
    print(atr)


#
print(dir(os) )