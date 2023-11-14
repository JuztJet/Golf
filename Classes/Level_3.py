import pygame
class Level3:
    def __init__(self, golf_ball, button, hole, mouse_pos, screen, width, height, dt, block, sand):
        self.golf_ball = golf_ball
        self.button  = button
        self.hole = hole
        self.mouse_pos = mouse_pos
        self.screen = screen
        self.width = width
        self.height = height
        self.block = block
        self.sand = sand

        self.dt = dt
    def create_objects(self):
        self.end_hole = self.hole(self.width/2-30,80, 55, 55, self.screen)
        #self.block1 = self.block(10, 310, 150, 20, self.screen, False)
        self.sand1 = self.sand(100,self.height-200,self.golf_ball, self.dt, 10, 50, 2000, self.screen)
        self.sand2 = self.sand(100,self.height-200,self.golf_ball, self.dt, self.width-10-100, 50, 2000, self.screen)
        self.sand3 = self.sand(self.width-20,50,self.golf_ball, self.dt, 10, 10, 2000, self.screen)
    def update(self):

        self.end_hole.update(self.golf_ball)
        #self.block1.update(self.golf_ball)
        self.sand1.update()
        self.sand2.update()
        self.sand3.update()
