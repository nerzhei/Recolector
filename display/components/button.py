__author__ = 'maicol'

import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, surface1, surface2, left=100, top=100):
        self._normal = surface1
        self._selected = surface2
        self._status = self._normal
        self._rect = self._status.get_rect()
        self._rect.left, self._rect.top = left, top

    def on_collide(self, display, cursor):
        if cursor.colliderect(self._rect):
            self._status = self._selected
        else:
            self._status = self._normal
        display.blit(self._status.get_surface(), self._rect)

    def on_click(self, cursor):
        if cursor.colliderect(self._rect):
            return True
        else:
            return False

    def set_rect(self, left, top):
        self._rect.left, self._rect.top = left, top

    def get_rect(self):
        return self._rect