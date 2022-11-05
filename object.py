import pygame as pg

class Object:
    def __init__(self, rect, color=(0, 0, 0)):
        self.rect = rect
        self.vel = [0, 0]
        self.color = color
    def move(self):
        self.rect[0] += self.vel[0]
        self.rect[1] += self.vel[1]
    def draw(self, surf):
        surf.blit(self.img, (self.rect[0], self.rect[1]))
