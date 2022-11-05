import pygame as pg
import player
import cube

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Stario Sisters")
player = player.Player([0, 0, 50, 50])
levels = [
    # (0, 0), (100, 0), (200, 0), (0, 100)
    [cube.Cube([i % 8 * 100, i // 8 * 100 + 400], [100, 100], (0, 0, 255)) for i in range(18)]
]
level = 0
clock = pg.time.Clock()
back = pg.Surface.convert_alpha(pg.image.load('imgs/back.png'))

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
    screen.fill((255, 0, 0))
    screen.blit(back, (0, 0))
    for cube in levels[level]:
        cube.draw(screen)
    player_move = 0
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        player_move -= 5
    if keys[pg.K_d]:
        player_move += 5
    if keys[pg.K_SPACE]:
        player.jump(levels[level])
    player.move(levels[level], player_move)
    player.draw(screen, (player_move + 5) / 10)
    pg.display.flip()
    clock.tick(60)
