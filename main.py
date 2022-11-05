import pygame as pg
import player
import cube

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Stario Sisters")
player = player.Player([0, 0, 50, 50])
levels = []
for i in range(1):
    new_list = []
    f = open(f"levels/{i}/level.txt")
    for y, line in enumerate(f):
        for x, thing in enumerate(line):
            if thing == 'c':
                new_list.append(cube.Cube((x * 100, y * 100), (0, 0, 0)))
    levels.append(new_list)
level = 0
stuff = {
    "level": levels[level],
    "objects": []
}
clock = pg.time.Clock()
back = pg.Surface.convert_alpha(pg.image.load('imgs/back.png'))

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
    screen.fill((255, 0, 0))
    screen.blit(back, (0, 0))
    for cube in stuff["level"]:
        cube.draw(screen)
    for obj in stuff["objects"]:
        obj.move(stuff)
        obj.draw(screen)
    player_move = 0
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        player_move -= 5
    if keys[pg.K_d]:
        player_move += 5
    if keys[pg.K_SPACE]:
        player.jump(levels[level])
    stuff["objects"] += player.move(stuff["level"], player_move)
    player.draw(screen, (player_move + 5) / 10)
    pg.display.flip()
    clock.tick(60)
