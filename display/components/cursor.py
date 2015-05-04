__author__ = 'maicol'

import pygame


class Cursor(pygame.Rect):
    def __init__(self):
         pygame.Rect.__init__(self, 0, 0, 0, 0)

    def update(self):
        self.left, self.top = pygame.mouse.get_pos()
