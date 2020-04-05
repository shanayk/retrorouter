import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
BG_COLOR = pg.Color('gray12')
img = pg.Surface((150, 150), pg.SRCALPHA)
pg.draw.polygon(img, (0, 100, 200), ((75, 0), (150, 75), (75, 150), (0, 75)))

def set_color(img, color):
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            color.a = img.get_at((x, y)).a  # Preserve the alpha value.
            img.set_at((x, y), color)  # Set the color of the pixel.

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_j:
                set_color(img, pg.Color(255, 0, 0))
            elif event.key == pg.K_h:
                set_color(img, pg.Color(0, 100, 200))

    screen.fill(BG_COLOR)
    screen.blit(img, (200, 200))
    pg.display.flip()
    clock.tick(60)
