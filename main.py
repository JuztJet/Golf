# Import
import pygame

# Getting necessary classes from files in folder called Classes
from Classes.Golf_Ball_Class import Golf_Ball
from Classes.Button_class import Button
from Classes.Block_class import Block
from Classes.Hole_class import Hole
from Classes.Level_Editor_Class import Level_Editor
from Classes.Level_1 import Level1
from Classes.Level_2 import Level2
from Classes.Level_3 import Level3
from Classes.Sand_class import Sand
from Classes.Slope_class import slope

pygame.init()  # Starting Pygame


screen = pygame.display.set_mode((1000, 700))  # Main windows called screen
window_w, window_h = pygame.display.get_desktop_sizes()[0]
w, h = (window_w/2-(350-20)/2)+10, (window_h/2-(570-20)/2)+10  # Getting width height
box_w, box_h = 330, 550

running = True
clock = pygame.time.Clock()
mouse_pos = pygame.mouse.get_pos()
dt = clock.tick(70) / 1000
time = 0  # Setting up a Time variable

golf_ball = Golf_Ball(-3.5, w+box_w * .5, h+box_h * .8, "White", 0.04593, dt, box_w, box_h, mouse_pos, screen,w, h)

# level1 = Level1(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt)
level2 = Level2(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope)  # Instantiating class called Level 2
# level3 = Level3(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, Sand)

level2.create_objects()  # Running method inside Level 2 which will create the objects (eg Blocks, golf hole)

# Pygame Loop
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            key = event.key
            if event.key == pygame.K_ESCAPE:
                running = False

    time += 2 * dt  # Time increase
    mouse_pos = pygame.mouse.get_pos()  # Updating mouse position
    screen.fill((107, 201, 97))

    grass = pygame.draw.rect(screen, 'Green', ((w, h), (box_w, box_h))) # Creating and drawing a grass
    # background

    # level3.update()

    level2.update(time, clock.get_fps())  # Updating level 2
    golf_ball.update(mouse_pos, dt)  # Updating the golf ball instance

    dt = clock.tick(60) / 1000
    clock.tick(60)

    # print(clock.get_fps())
    pygame.display.flip()