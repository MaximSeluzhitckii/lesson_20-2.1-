import random
import pygame as pg

pg.init()

is_jump = False
jump_counter = 2


class Circle:
    def __init__(self, color, circle_radius, x, y, speed):
        self.color = color
        self.circle_radius = circle_radius
        self.x = x
        self.y = y
        self.speed = speed
        self.dir_h = 'right'
        self.dir_v = 'up'

    def draw(self):
        pg.draw.circle(win, self.color, (self.x, self.y), self.circle_radius)

    def move_by_kyes(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.x -= self.speed
        elif keys[pg.K_RIGHT]:
            self.x += self.speed
        elif keys[pg.K_UP]:
            self.y -= self.speed
        elif keys[pg.K_DOWN]:
            self.y += self.speed

    def horizontal_movement(self, weight):
        if self.dir_h == 'right':
            self.x += self.speed
            if self.x > weight:
                self.dir_h = 'left'
        else:
            self.x -= self.speed
            if self.x < 0:
                self.dir_h = 'right'

    def vertical_movement(self, height):
        if self.dir_v == 'up':
            self.y += self.speed
            if self.y > height:
                self.dir_v = 'down'
        else:
            self.y -= self.speed
            if self.y < 0:
                self.dir_v = 'up'


height = 500
weight = 500

FPS = 120
clock = pg.time.Clock()

TIMEREVENT = pg.USEREVENT + 1
pg.time.set_timer(TIMEREVENT, 3000)

win = pg.display.set_mode((weight, height))
circle1 = Circle('yellow', 20, 250, 250, 2)

circle100 = []
x = 0
for i in range(100):
    a = Circle('yellow', 20, x, 250, 2)
    circle100.append(a)
    x += 100


# for i in range(100):
#     a = Circle(random.choices(range(256), k=3), 20, i * 10, i * 5, 2)
#     circle100.append(a)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        if event.type == TIMEREVENT:
            circle100.append(Circle(random.choices(range(256), k=3), 30, random.randrange(weight), random.randrange(height), 10))
            print(len(circle100))

    win.fill((255, 255, 255))
    circle1.move_by_kyes()
    circle1.draw()
    pg.display.update()
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        is_jump = True

    if is_jump is True:
        if jump_counter >= -30:
            circle1.y -= jump_counter
            jump_counter -= 2
        else:
            jump_counter = 30
            is_jump = False

    for i in circle100:
        i.horizontal_movement(weight)
        i.vertical_movement(height)
        i.draw()
    pg.display.update()

    # pg.time.delay(10)
    clock.tick(FPS)
