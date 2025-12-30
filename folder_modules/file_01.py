#!/usr/bin/env python3 
import os
 
 
print("Print from file_01.py!")
print(os.path.dirname(os.path.abspath(__file__))) # root current folder
print(__name__) 
__counter = 0 # convention for saying do not modify it, but it possible
 
 
def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum
 
 
def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod
 
 
 
my_list = [i+1 for i in range(5)]
print(suml(my_list) == 15)
print(prodl(my_list) == 120) 