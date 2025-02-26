import pygame
import constants as cn


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {cn.SCREEN_WIDTH}")
    print(f"Screen height: {cn.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((cn.SCREEN_WIDTH, cn.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # game loop
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        # Store time in seconds within dt, side effect set to 60fps using .tick()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
