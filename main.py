import folder_modules.file_01 as file_01
import sys

# add new route module
sys.path.append(r"C:\Users\*****\*****\new-python-02")
for p in sys.path:
  print(p) 

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(file_01.suml(zeroes))
print(file_01.prodl(ones)) 

 