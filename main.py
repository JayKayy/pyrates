""" Pyrates: Exploration, Liberty and Bounty for all! """
import pygame


pygame.init()

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
OCEAN = (0, 230, 230)

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Pyrates!')
CLOCK = pygame.time.Clock()

SHIP_IMG = pygame.image.load('images/ship.png')
ISLAND_UN = pygame.image.load('images/island_uninhabited.png')
ISLAND_TYPES = {'uninhabited': ISLAND_UN}

X_MIN = 0
X_MAX = (DISPLAY_WIDTH - SHIP_IMG.get_size()[0])
Y_MIN = 0
Y_MAX = (DISPLAY_HEIGHT - SHIP_IMG.get_size()[1])


def ship(pos_x, pos_y):
    """ Draw the pirate ship """
    if pos_x < X_MIN:
        pos_x = X_MIN
    if pos_x > X_MAX:
        pos_x = X_MAX
    if pos_y < Y_MIN:
        pos_y = Y_MIN
    if pos_y > Y_MAX:
        pos_y = Y_MAX
    GAME_DISPLAY.blit(SHIP_IMG, (pos_x, pos_y))


def island(island_type, pos_x, pos_y):
    """ Draw an island """
    if island_type not in ISLAND_TYPES:
        print("ERROR: Invalid Island type")
    else:
        GAME_DISPLAY.blit(ISLAND_TYPES[island_type], (pos_x, pos_y))


def game_loop():
    """ Main game loop """

    ship_x = (DISPLAY_WIDTH * 0.45)
    ship_y = (DISPLAY_HEIGHT * 0.2)

    island_x = (DISPLAY_WIDTH * 0.75)
    island_y = (DISPLAY_HEIGHT * 0.2)

    x_change = 0
    y_change = 0
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        ship_x += x_change
        ship_y += y_change
        GAME_DISPLAY.fill(OCEAN)
        island('uninhabited', island_x, island_y)
        ship(ship_x, ship_y)
        pygame.display.update()
        CLOCK.tick(60)


game_loop()

pygame.quit()
quit()
