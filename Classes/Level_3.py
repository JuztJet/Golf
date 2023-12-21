import pygame
class Level3:
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
        self.sand = sand

        self.dt = dt
    def create_objects(self):
        #Creating the objects
        self.end_hole = self.hole(self.box_width+(self.width/2),self.box_height+180, 55, 55, self.screen)
        self.block1 = self.block(self.box_width+50, self.box_height+110, 20, 120, self.screen, False, self.dt,0, 0, False, self.box_width+50, self.box_width+300, 500)
        self.block2 = self.block(self.box_width, self.box_height+360, 170, 20, self.screen, False, self.dt,0, 0, False, self.box_width+50, self.box_width+300, 500)
        self.block3 = self.block(self.box_width+270, self.box_height+110, 20, 120, self.screen, False, self.dt,0, 0, False, self.box_width+50, self.box_width+300, 500)
        self.block4 = self.block(self.box_width+50, self.box_height+110, 240, 20, self.screen, False, self.dt,0, 0, False, self.box_width+50, self.box_width+300, 500)
        self.block5 = self.block(self.box_width+200, self.box_height+230, 30, 20, self.screen, False, self.dt,0, 0, True, self.box_width+90, self.box_width+240, 200)
        # self.power_up_1 = self.power_up(self.box_width+150, self.box_height+150, self.golf_ball, "Slow", self.screen, False)
        # self.water_1 = self.water(self.box_width+50, self.box_height+50, 100, 50, self.screen, 0)
        # self.roto_block = self.corner_block(self.box_width+250
        #                                     , self.box_height+250, 120, 20, self.screen, False, self.dt, -135)
    def update(self, time, clock):
        #Updating the objects, each object has their own specific update code
        self.end_hole.update(self.golf_ball)
        self.block1.update(self.golf_ball)
        self.block2.update(self.golf_ball)
        self.block3.update(self.golf_ball)
        self.block4.update(self.golf_ball)
        self.block5.update(self.golf_ball)

        self.block1.ccd(self.golf_ball)
        self.block2.ccd(self.golf_ball)
        self.block3.ccd(self.golf_ball)
        self.block4.ccd(self.golf_ball)
        self.block5.ccd(self.golf_ball)