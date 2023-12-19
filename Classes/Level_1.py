import pygame
class Level1:
    def __init__(self, golf_ball, button, hole, mouse_pos, screen, width, height, dt, block,box_width, box_height, slope, power_up, water, corner_block, sand, time):

        #Contains classes from many different files, (eg block_class from block_class file)
        self.golf_ball = golf_ball

        self.width = box_width
        self.height = box_height

        self.button  = button
        self.hole = hole
        self.mouse_pos = mouse_pos
        self.screen = screen
        self.time = time
        self.box_width = width
        self.box_height = height

        self.block = block
        self.slope = slope
        self.power_up = power_up
        self.water = water
        self.corner_block = corner_block
        self.sand = sand

        self.dt = dt
        self.fake_brick = pygame.transform.smoothscale(pygame.image.load('Assets/Wooden_Block.png'), (self.width, 30))
    def create_objects(self):
        #Creating the objects
        self.end_hole = self.hole(self.box_width+(self.width/2),self.box_height+80, 55, 55, self.screen)

    def update(self, time, clock):
        #Updating the objects, each object has their own specific update code
        self.end_hole.update(self.golf_ball)


        #self.down_slope.update()
        #self.sand.update()
        #self.power_up_1.update()
        #self.water_1.update(self.golf_ball)
        #print(self.golf_ball.angle)
        #self.roto_block.update(self.golf_ball)
        #self.block2.update(self.golf_ball, time, clock)