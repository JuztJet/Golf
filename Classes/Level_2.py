import pygame
class Level2:
    def __init__(self, golf_ball, button, hole, mouse_pos, screen, width, height, dt, block,box_width, box_height, slope):

        #Contains classes from many different files, (eg block_class from block_class file)
        self.golf_ball = golf_ball
        self.box_width = box_width
        self.box_height = box_height
        self.button  = button
        self.hole = hole
        self.mouse_pos = mouse_pos
        self.screen = screen
        self.box_width = width
        self.box_height = height
        self.block = block
        self.slope = slope

        self.dt = dt
    def create_objects(self):
        #Creating the objects
        #self.end_hole = self.hole(self.width/2-100,50, 55, 55, self.screen)
        self.block1 = self.block(self.box_width+200, self.box_height+310, 50, 20, self.screen, False, self.dt,0, 0, True, self.box_width+50, self.box_width+300, 500)
        self.down_slope = self.slope(self.box_width+50, self.box_height+50, self.golf_ball, 100, 100, "Down", self.screen)
        #self.block2 = self.block(self.width-160, 220, 150, 20, self.screen, False, self.dt,0,0)
    def update(self, time, clock):
        #Updating the objects, each object has their own specific update code
        #self.end_hole.update(self.golf_ball)
        #self.block1.update(self.golf_ball, time, clock)
        self.down_slope.update()
        #self.block2.update(self.golf_ball, time, clock)