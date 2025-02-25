import pygame
import constants as cn


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {cn.SCREEN_WIDTH}")
    print(f"Screen height: {cn.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((cn.SCREEN_WIDTH, cn.SCREEN_HEIGHT))
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()


if __name__ == "__main__":
    main()
