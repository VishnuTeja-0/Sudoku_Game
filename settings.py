import pygame
import random
from PuzzleList import testBoard_list

pygame.init()

WIDTH = 600
HEIGHT = 600

#colours
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTBLUE = (96,216,232)
LOCKEDCELLCOLOUR = (189,189,189)
GREEN = (0,128,0)

#testBoard, psuedo-randomly generated
k = random.randint(0,len(testBoard_list))
testBoard2 = testBoard_list[k]

#postions and sizes
gridPos = (75,100)
cellSize = 50
gridSize = cellSize*9

#fonts
smallText = pygame.font.SysFont("Arial", 20)
largeText = pygame.font.SysFont("Arial", 120)
