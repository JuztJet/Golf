import pygame
class Level1:
    def __init__(self, golf_ball, button, hole, mouse_pos, screen, width, height, dt):
        self.golf_ball = golf_ball
        self.button  = button
        self.hole = hole
        self.mouse_pos = mouse_pos
        self.screen = screen
        self.width = width
        self.height = height

        self.dt = dt
    def create_objects(self):
        self.end_hole = self.hole(self.width/2-20,50, 55, 55, self.screen)
    def update(self):
        self.create_objects()
        self.end_hole.update(self.golf_ball)