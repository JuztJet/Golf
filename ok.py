import pygame
pygame.init() #Start Pygame

screen = pygame.display.set_mode((640,480)) #Start the screen
image = pygame.image.load('Assets/golf.png').convert_alpha()
rect = image.get_rect(center = (640/2, 480/2))
x = 320
y = 240
x2 = 0
running = True
while running:
    screen.fill('white')
    image_copy = pygame.transform.rotate(image, x2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #The user closed the window!
            running = False #Stop running
    screen.blit(image_copy, (x-int(image_copy.get_width()/2),y-int(image_copy.get_height()/2)))
    pygame.display.flip()
    x2+=0.1
    print(x2)
pygame.quit() #Close the window