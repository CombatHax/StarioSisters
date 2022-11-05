from object import *

class Player(Object):
    def __init__(self, pos):
        self.rect = pos
        self.dire = 1
        things = ['imgs/dude-left.png', 'imgs/dude-right.png']
        self.img = [pg.Surface.convert_alpha(pg.image.load(things[i])) for i in range(2)]
        self.vel = [0, 0]
    def move(self, level, movement):
        self.vel[1] += 0.1
        self.rect[0] += self.vel[0] + movement
        collision = self.check_collision(level)
        if not collision[1]:
            self.rect[1] += self.vel[1]
        else:
            self.vel[1] = 0
            self.rect[1] = self.rect[1]
        print(self.rect)
    def jump(self, level):
        if self.check_collision(level)[1]:
            self.vel[1] -= 5
            self.rect[1] -= 0.1
    def check_collision(self, level):
        collide = [0, 0, 0, 0]
        for cube in level:
            if cube.rect[0] <= self.rect[0] <= cube.rect[0] + cube.rect[3]:
                if self.rect[1] + self.rect[3] >= cube.rect[1]:
                    if self.rect[1] + self.rect[3] <= cube.rect[1] + cube.rect[3]:
                        collide[1] = 1
                        self.rect[1] = cube.rect[1] - self.rect[3]
        return collide
    def draw(self, surf, dire):
        if dire != 0.5:
            self.dire = int(dire)
        surf.blit(self.img[self.dire], (self.rect[0], self.rect[1]))
