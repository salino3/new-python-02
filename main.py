import folder_modules.file_01 as file_01
import sys
import pygame

# add new route module
# sys.path.append(r"C:\Users\*****\*****\new-python-02")
# for p in sys.path:
#   print(p) 

# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(file_01.suml(zeroes))
# print(file_01.prodl(ones)) 


    # pip help operation – shows a brief description of pip;
    # pip list – shows a list of the currently installed packages;
    # pip show package_name – shows package_name info including the package's dependencies;
    # pip search anystring – searches through PyPI directories in order to find packages whose names contain anystring;
    # pip install name – installs name system-wide (expect problems when you don't have administrative rights);
    # pip install --user name – installs name for you only; no other platform user will be able to use it;
    # pip install -U name – updates a previously installed package;
    # pip uninstall name – uninstalls a previously installed package.

########################################################
# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#   for event in pygame.event.get():
#    if event.type == pygame.QUIT\
#    or event.type == pygame.MOUSEBUTTONUP\
#    or event.type == pygame.KEYUP:
#     run = False


 # Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space
char_3 = 'ę'

print(ord(char_1))
print(ord(char_2))
print(ord(char_3))

# If you know the code point (number) and want to get the 
# corresponding character, you can use a function named chr().

print(chr(97))
print(chr(945))

# min() return letter in a string for unicode value

people = [
    {"name": "Ana", "age": 30},
    {"name": "Luis", "age": 25},
    {"name": "Marta", "age": 28}
]

print(min(people, key=lambda p: p["age"])) # {'name': 'Luis', 'age': 25}

t = [0, 1, 2, -3] # TypeError: '>' not supported between instances of 'str' and 'int'
print(max(t)) # 2

# Demonstrating the index() method: #> error if doesn't find anything
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA3".index("bB")) # 2

# Demonstrating the list() function:
print(list("abcabc")) # ['a', 'b', 'c', 'a', 'b', 'c']
print(list(range(4))) # [0, 1, 2, 3]
print(list(tuple(range(4)))) # [0, 1, 2, 3]

# The count() method counts all occurrences of the element inside the sequence.
# The absence of such elements doesn't cause any problems.

print("abcabc".count("b"))
print('abcabc'.count("d")) # 0




