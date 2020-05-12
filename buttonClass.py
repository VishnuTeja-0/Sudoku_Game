import pygame
from SolveFunction import *
from settings import *

class Button:
    def __init__(self, x, y, width, height, text= None, colour=(73,73,73), highlightedColour=(189,189,189), function=None, params=None):
        self.image = pygame.Surface((width,height))
        self.pos = (x,y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = text
        self.colour = colour
        self.highlightedColour = highlightedColour
        self.function = function
        self.params = params
        self.highlighted = False
        self.height = height
        self.width = width

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self, window):
        if self.highlighted:
            self.image.fill(self.highlightedColour)
        else:
            self.image.fill(self.colour)
        window.blit(self.image, self.pos)
        
        
    def isClicked(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.pos[0] + self.width > mouse[0] > self.pos[0] and self.pos[1] + self.height > mouse[1] > self.pos[1]:
            if click[0] == 1:
                return True
        return False
    