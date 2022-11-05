import pygame as pg
import object

class Coin(object.Object):
    def __init__(self, pos):
        self.vel = [0, -5]
        img = pg.image.load("imgs/coin.png")
        self.img = pg.transform.scale(img, (50, 50))
        size = self.img.get_size()
        self.rect = pos + list(size)