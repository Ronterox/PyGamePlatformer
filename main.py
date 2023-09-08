import pygame
from pygame.surface import Surface
from pygame.font import Font
from enum import IntEnum

pygame.init()
pygame.display.set_caption("Ninja Saga")


class Key(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Player:
    movement: list[int] = [0, 0, 0, 0]

    def __init__(self, img: Surface, position: list[int]):
        self.img = img
        self.position = position


def close_window():
    pygame.quit()
    quit()


screen: Surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = Font("freesansbold.ttf", 32)

img = pygame.image.load("assets/images/clouds/cloud_1.png")
img.set_colorkey((0, 0, 0))

player = Player(img,  [100, 200])
collision_zone = pygame.Rect(50, 100, 100, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window()
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP | pygame.K_w:
                    player.movement[Key.UP] = 5
                case pygame.K_DOWN | pygame.K_s:
                    player.movement[Key.DOWN] = 5
                case pygame.K_LEFT | pygame.K_a:
                    player.movement[Key.LEFT] = 5
                case pygame.K_RIGHT | pygame.K_d:
                    player.movement[Key.RIGHT] = 5
                case pygame.K_ESCAPE:
                    close_window()
                case _:
                    pass
        elif event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_UP | pygame.K_w:
                    player.movement[Key.UP] = 0
                case pygame.K_DOWN | pygame.K_s:
                    player.movement[Key.DOWN] = 0
                case pygame.K_LEFT | pygame.K_a:
                    player.movement[Key.LEFT] = 0
                case pygame.K_RIGHT | pygame.K_d:
                    player.movement[Key.RIGHT] = 0
                case _:
                    pass

    player.position[1] += player.movement[Key.DOWN] - player.movement[Key.UP]
    player.position[0] += player.movement[Key.RIGHT] - player.movement[Key.LEFT]

    screen.fill((0x5b, 0xb4, 0xdd))  # 0x5bb4dd
    
    player_collider = pygame.Rect(*player.position, *player.img.get_size()) # type: ignore
    red = round(0xFF * 0.5) if player_collider.colliderect(collision_zone) else 0xFF
    pygame.draw.rect(screen, (red, 0, 0), collision_zone)

    screen.blit(player.img, player.position)

    fps: Surface = font.render("FPS: " + str(int(clock.get_fps())), True, (255, 255, 255))
    screen.blit(fps, (0, 0))

    pygame.display.update()
    clock.tick(144)
