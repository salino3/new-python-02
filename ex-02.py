import random  

my_list = [1, 2, 3, -4.8, 5.9, 6, 7, 8, 9, 10, 3, 400, 5, 6, 7, 8, 9, 10]

# choose one element or a list of elements ramdomnly
print(random.choice([my_list]))
# print(random.choice([])) # Error
print(random.sample(my_list, 5))
print(random.sample(my_list, 1))
print(random.sample(my_list, 0))