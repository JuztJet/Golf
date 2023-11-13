import pygame
import math


class Level_Editor:
    def __init__(self, mouse_pos, screen, w, h, golf_ball, Button, Hole, Block, dt):
        self.font = pygame.font.SysFont(None, 20)
        self.mouse_pos = mouse_pos
        self.screen = screen
        self.golf_ball = golf_ball
        self.Button = Button
        self.Hole = Hole
        self.Block = Block
        self.w = w
        self.h = h
        self.level_edit = False
        self.blocks = []

        self.text = self.font.render('', True, ('Black'))
        self.font.point_size = 13
        self.key = self.font.render("Q=Level Edit mode|S=Scale|M=Move\nEnd=Adjust size increments|"
                                    "Delete=delete\nD=Duplicate", True, ('Black'))
        self.button_selected_clicked = False
        self.selected_item = ''
        self.dt = dt
        self.mode = ''
        self.mode_colour = 'Black'
        self.move_value = 10
        self.touching_block = False
        self.touching_block2 = ''
        self.side = ''
    def level_edit_mode(self):
        self.edit_layer = pygame.Surface((self.w-20, self.h-20))
        self.edit_layer.set_alpha(100)
        self.edit_layer.fill('Blue')
    def add_block(self, pos):
        block = self.Block(pos[0], pos[1], 20, 20, self.screen, False)
        self.blocks.append(block)
        print('Block has been added')
        self.selected_item = block
        self.text = self.font.render('Editing a block', True, ('Black'))
        print('Block, top left pos={}, top right = {}, bottom right={}, bottom left ={}, width& height = {}'.format(
            block.rect.topleft,
            block.rect.topright, block.rect.bottomright, block.rect.bottomleft
            , (block.rect.width, block.rect.height)))

    def selector(self, mouse_pos):
        for block in self.blocks:
            if block.rect.collidepoint(mouse_pos):
                self.selected_item = block
                if self.mode !='Scale' and self.mode!='Move':
                    self.text = self.font.render('Editing a block', True, ('Black'))

    def item_identifier(self, mouse_pos):
        for block in self.blocks:
            if block.rect.collidepoint(mouse_pos):

                print('Block, top left pos={}, top right = {}, bottom right={}, bottom left ={}, width& height = {}'.format(block.rect.topleft,
                                                                            block.rect.topright, block.rect.bottomright, block.rect.bottomleft
                                                                           ,(block.rect.width, block.rect.height)))


    def block_modifier(self, key):


        if key == pygame.K_s:
            self.mode = 'Scale'
            self.mode_colour = 'Green'

            self.text = self.font.render('Scaling a Block', True, ('Black'))
            self.text = self.font.render("{} is used at {}px".format(self.mode, self.move_value), True, ('Black'))
            self.side = 'Top'

        elif key == pygame.K_m:
            self.mode = 'Move'
            self.mode_colour = 'Yellow'
            self.text = self.font.render("{} is used at {}px".format(self.mode, self.move_value), True, ('Black'))
        elif key == pygame.K_END and self.move_value==10:
            self.move_value = 1
            self.text = self.font.render("{} is used at 1px".format(self.mode), True, ('Black'))
        elif key == pygame.K_END and self.move_value==1:
            self.move_value = 10
            self.text = self.font.render("{} is used at 10px".format(self.mode), True, ('Black'))


        if self.mode == 'Scale':
            if key == pygame.K_LEFT:
                if self.selected_item.rect.width >20:
                    self.selected_item.image = pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png'), (self.selected_item.rect.width-self.move_value, self.selected_item.rect.height))
                    self.selected_item.rect.width -= self.move_value
                    print(self.selected_item.rect.width)
            elif key == pygame.K_RIGHT:
                if self.selected_item.rect.width <350:
                    self.selected_item.image = pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png'), (
                    self.selected_item.rect.width + self.move_value, self.selected_item.rect.height))
                self.selected_item.rect.width += self.move_value
            elif key == pygame.K_UP:
                if self.selected_item.rect.height >19:
                    self.selected_item.image = pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png'), (self.selected_item.rect.width, self.selected_item.rect.height-self.move_value))
                    self.selected_item.rect.height -= self.move_value
                    print(self.selected_item.rect.height)
            elif key == pygame.K_DOWN:
                if self.selected_item.rect.height <350:
                    self.selected_item.image = pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png'), (
                    self.selected_item.rect.width, self.selected_item.rect.height + self.move_value))
                    self.selected_item.rect.height += self.move_value

        elif self.mode == 'Move':
            if key == pygame.K_LEFT:
                if self.selected_item.rect.left >=10:
                    self.selected_item.rect.x -= self.move_value
                    print(self.selected_item.rect.x)
                if self.selected_item.rect.left<10:
                    self.selected_item.rect.x = 10
            elif key == pygame.K_RIGHT:
                if self.selected_item.rect.left+self.selected_item.width <=self.w-20:
                    self.selected_item.rect.x += self.move_value
                    print(self.selected_item.rect.x)
                if self.selected_item.rect.x+self.selected_item.width >self.w-20:
                    self.selected_item.rect.x = self.w-10-self.selected_item.width
            elif key == pygame.K_UP:
                if self.selected_item.rect.top >=10:
                    self.selected_item.rect.y -= self.move_value
                    print(self.selected_item.rect.y)
                if self.selected_item.rect.top<10:
                    self.selected_item.rect.y = 10
            elif key == pygame.K_DOWN:
                if self.selected_item.rect.bottom <=self.h-20:
                    self.selected_item.rect.y += self.move_value
                    print(self.selected_item.rect.y)
                if self.selected_item.rect.bottom >self.h-20:
                    self.selected_item.rect.bottom = self.h-10

        if key == pygame.K_DELETE:
            for block in self.blocks:
                if block == self.selected_item:
                    self.blocks.remove(block)
                    self.selected_item = ''
                    self.mode = ''
                    self.mode_colour = 'Black'
                    self.text = self.font.render('', True, ('Black'))

                    return
        if key == pygame.K_d:
            block = self.Block(self.selected_item.rect.x, self.selected_item.rect.y, self.selected_item.rect.width, self.selected_item.rect.height, self.screen, False)
            self.blocks.append(block)
            self.selected_item = block
            print(2)

        for blockr in self.blocks:

            if blockr.rect.colliderect(self.selected_item.rect) and blockr!=self.selected_item and self.touching_block == False:
                if self.touching_block:
                    break
                if self.touching_block == False:
                    self.touching_block = True
                    self.touching_block2 = blockr

                    print('Block is being touched')
                    break

            elif self.touching_block and blockr!=self.selected_item and self.touching_block2.rect.colliderect(self.selected_item.rect)==False:
                self.touching_block = False
                print(2)




    def key_board_manager(self, event, mouse_pos):
        if event.key == pygame.K_q:
            if self.level_edit==False:
                self.level_edit= True
            else:
                self.level_edit = False
        elif event.key==pygame.K_w and self.level_edit:
            self.add_block(mouse_pos)
            self.mode_colour = 'Black'
            self.mode = ''


    def update(self, mouse_pos, key):
        if self.level_edit:
            if self.button_selected_clicked:
                self.button_selected_clicked = False
                self.selector(mouse_pos)
                self.item_identifier(mouse_pos)
            self.screen.blit(self.edit_layer, (10,10))
            for block in self.blocks:
                self.screen.blit(block.image, block.rect)

            self.screen.blit(self.text, (20, self.h-40))

            if self.selected_item != '':
                #pygame.draw.rect(self.screen, self.mode_colour, self.selected_item.rect, 1)
                if self.side =='Top':
                    pygame.draw.line(self.screen, self.mode_colour, self.selected_item.rect.topleft, self.selected_item.rect.topright, 2)
                elif self.side =='Bottom':
                    pygame.draw.line(self.screen, self.mode_colour, self.selected_item.rect.bottomleft, self.selected_item.rect.bottomright, 2)
                elif self.side =='Left':
                    pygame.draw.line(self.screen, self.mode_colour, self.selected_item.rect.topleft, self.selected_item.rect.bottomleft, 2)
                else:
                    pygame.draw.line(self.screen, self.mode_colour, self.selected_item.rect.topright, self.selected_item.rect.bottomright, 2)

                self.block_modifier(key)
            self.screen.blit(self.key, (20, self.h - 100))


