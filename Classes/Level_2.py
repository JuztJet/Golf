import pygame
class Level2:
    def __init__(self, golf_ball, button, hole, mouse_pos, screen, width, height, dt, block):
        self.golf_ball = golf_ball
        self.button  = button
        self.hole = hole
        self.mouse_pos = mouse_pos
        self.screen = screen
        self.width = width
        self.height = height
        self.block = block

        self.dt = dt
    def create_objects(self):
        self.end_hole = self.hole(self.width/2-100,50, 55, 55, self.screen)
        self.block1 = self.block(10, 310, 150, 20, self.screen, False, self.dt,0, 0)
        self.block2 = self.block(self.width-160, 220, 150, 20, self.screen, False, self.dt,0,0)
    def update(self, time, clock):
        #self.create_objects()
        self.end_hole.update(self.golf_ball)
        self.block1.update(self.golf_ball, time, clock)
        self.block2.update(self.golf_ball, time, clock)