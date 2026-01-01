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


run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
  for event in pygame.event.get():
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    run = False



 