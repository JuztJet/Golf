import pygame


class Level5:
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
        self.fake_brick = pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png'), (self.width, 30))
    def create_objects(self):
        #Creating the objects
        self.end_hole = self.hole(self.box_width+(self.width/2),self.box_height+80, 55, 55, self.screen)
        self.button_1 = self.button(self.box_width+50, self.box_height+300, "Enabled", 'Flat', False, self.screen, False, self.block, self.box_width, self.box_height, self.dt, self.time)
        self.button_2 = self.button(self.box_width+200, self.box_height+300, "Enabled", 'Flat', True, self.screen, True, self.block, self.box_width, self.box_height, self.dt, self.time)
    def update(self, time, clock):
        #Updating the objects, each object has their own specific update code
        self.end_hole.update(self.golf_ball)
        self.button_1.update(self.golf_ball)
        self.button_2.update(self.golf_ball)
        self.screen.blit(self.fake_brick, (self.box_width, self.box_height + 180))

        if self.button_2.disable_after_use and self.button_2.mode != 'Enabled':
            self.button_2.wall[0].ccd(self.golf_ball)
            self.button_2.wall[1].ccd(self.golf_ball)
            self.button_2.wall[2].ccd(self.golf_ball)
            self.button_2.wall[3].ccd(self.golf_ball)


        #self.down_slope.update()
        #self.sand.update()
        #self.power_up_1.update()
        #self.water_1.update(self.golf_ball)
        #print(self.golf_ball.angle)
        #self.roto_block.update(self.golf_ball)
        #self.block2.update(self.golf_ball, time, clock)