import pygame
pygame.init()

from Env_wPygame import *
from Q_Learning import *

colors = {"blue": (20, 81, 232), "red": (238, 34, 24), "green":( 0, 252, 8)}

Size = (600,600)

#Win = pygame.display.set_mode(Size)
#pygame.display.set_caption("Environnement")

def update_win():
    pygame.display.update()

def main(Size, colors):
    run = True
    print("main")
    QLearning(Episodes, Size, colors)



main(Size, colors)
#test()
