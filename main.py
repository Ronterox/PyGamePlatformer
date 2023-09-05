import pygame
from pygame.surface import Surface
from pygame.font import Font

pygame.init()

pygame.display.set_caption("Ninja Saga")
screen: Surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = Font("freesansbold.ttf", 32)

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit() 
            
    fps: Surface = font.render("FPS: " + str(int(clock.get_fps())), True, (255, 255, 255))
    screen.blit(fps, (0, 0))
    
    pygame.display.update()
    clock.tick(144)