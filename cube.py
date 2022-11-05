import pygame as pg
import object

class Cube(object.Object):
    def __init__(self, pos, size, color) -> None:
        self.rect = pos + size
        self.color = color
        self.img = pg.image.load("imgs/cube.png")
