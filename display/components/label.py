__author__ = 'maicol'

import pygame


class Label(pygame.Rect):
    def __init__(self, font, text, color, background=None):
        self._font = font
        self._color = color
        self._background = background
        self._text = self._font.render(text, 0, self._color, self._background)

    def update(self, display, x, y):
        display.blit(self._text, (x, y))

    def get_rect(self):
        return self._text.get_rect()

    def get_surface(self):
        return self._text

    def set_text(self, text):
        self._text = self._font.render(text, 0, self._color, self._background)