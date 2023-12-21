import pygame
class Level2:
    def __init__(self, golf_ball, button, hole, mouse_pos, screen, width, height, dt, block,box_width, box_height, slope, power_up, water, corner_block, sand):

        #Contains classes from many different files, (eg block_class from block_class file)
        self.golf_ball = golf_ball

        self.width = box_width
        self.height = box_height

        self.button  = button
        self.hole = hole
        self.mouse_pos = mouse_pos
        self.screen = screen

        self.box_width = width
        self.box_height = height

        self.block = block
        self.slope = slope
        self.power_up = power_up
        self.water = water
        self.corner_block = corner_block
        self.Sand = sand

        self.dt = dt
    def create_objects(self):
        #Creating the objects
        self.end_hole = self.hole(self.box_width+(self.width/2),self.box_height+50, 55, 55, self.screen)
        self.sand = self.Sand(180, 240, self.golf_ball, self.dt, self.box_width, self.box_height+140, 590, self.screen)
        self.down_slope = self.slope(self.box_width+180, self.box_height+120, self.golf_ball, 150, 300, "Down", self.screen, 1.5)
    def update(self, time, clock):
        #Updating the objects, each object has their own specific update code
        self.end_hole.update(self.golf_ball)

        self.down_slope.update()
        self.sand.update()
