import pygame as pg
import object

class Cube(object.Object):
    def __init__(self, pos, color) -> None:
        self.rect = pos + (100, 100)
        self.color = color
        self.img = pg.image.load("imgs/cube.png")
        print(self.rect)
