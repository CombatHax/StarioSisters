import pygame as pg

class Object:
    def __init__(self, rect, img: pg.Surface, color=(0, 0, 0)):
        size = img.get_size()
        self.rect = rect + size
        self.vel = [0, 0]
        self.color = color
        self.img = img
    def move(self, stuff):
        if self.rect[1] >= 600:
            stuff["objects"].remove(self)
        self.vel[1] += 0.25
        self.rect[0] += self.vel[0]
        self.rect[1] += self.vel[1]
    def draw(self, surf):
        surf.blit(self.img, (self.rect[0], self.rect[1]))
