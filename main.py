""" Pyrates: Exploration, Liberty and Bounty for all! """
import random
import pygame
from lib.island import Island
from lib.coin import Coin

pygame.init()

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
OCEAN = (0, 230, 230)

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Pyrates!')
CLOCK = pygame.time.Clock()

SHIP_IMG = pygame.image.load('images/ship.png')
COIN_IMG = pygame.image.load('images/pirate_coin.png')
ISLAND_UN = pygame.image.load('images/island_uninhabited.png')
ISLAND_TYPES = {'uninhabited': ISLAND_UN}
ISLAND_NAMES = ['Nassau', 'Port Royal', 'Tortuga']
# Populated at runtime
ISLANDS = []
COINS = []
SHIP_X_MIN = 0
SHIP_X_MAX = (DISPLAY_WIDTH - SHIP_IMG.get_size()[0])
SHIP_Y_MIN = 0
SHIP_Y_MAX = (DISPLAY_HEIGHT - SHIP_IMG.get_size()[1])

ISLAND_X_MIN = 0
ISLAND_X_MAX = (DISPLAY_WIDTH - ISLAND_UN.get_size()[0])
ISLAND_Y_MIN = 0
ISLAND_Y_MAX = (DISPLAY_HEIGHT - ISLAND_UN.get_size()[1])

COIN_X_MIN = 0
COIN_X_MAX = (DISPLAY_WIDTH - COIN_IMG.get_size()[0])
COIN_Y_MIN = 0
COIN_Y_MAX = (DISPLAY_HEIGHT - COIN_IMG.get_size()[1])

def draw_ship(pos_x, pos_y):
    """ Draw the pirate ship """
    if pos_x < SHIP_X_MIN:
        pos_x = SHIP_X_MIN
    if pos_x > SHIP_X_MAX:
        pos_x = SHIP_X_MAX
    if pos_y < SHIP_Y_MIN:
        pos_y = SHIP_Y_MIN
    if pos_y > SHIP_Y_MAX:
        pos_y = SHIP_Y_MAX
    GAME_DISPLAY.blit(SHIP_IMG, (pos_x, pos_y))


def draw_coin(c):
    """ Draw the pirate coin """
    GAME_DISPLAY.blit(COIN_IMG, (c.get_x(), c.get_y()))

def draw_island(island):
    """ Draw an island """
    if island.get_island_type() not in ISLAND_TYPES:
        print(island.get_island_type())
        print("ERROR: Invalid Island type")
    else:
        GAME_DISPLAY.blit(
            ISLAND_TYPES[island.get_island_type()], (island.get_x(), island.get_y()))


def ship_event(ship_x, ship_y):
    """ Detect if the ship has landed on an item """
    # Modify ship_x and ship_y to calculate from the center of the ship
    ship_x += (SHIP_IMG.get_size()[0]/2)
    ship_y += (SHIP_IMG.get_size()[1]/2)

    for isle in ISLANDS:
        isle_x = isle.get_x()
        isle_y = isle.get_y()
        # topLeft
        if isle_x <= ship_x <= (isle_x + ISLAND_UN.get_size()[0]):
            if isle_y <= ship_y <= (isle_y + ISLAND_UN.get_size()[1]):
                return True, isle

    for coin in COINS:
        coin_x = coin.get_x()
        coin_y = coin.get_y()
        if coin_x <= ship_x <= (coin_x + COIN_IMG.get_size()[0]):
            if coin_y <= ship_y <= (coin_y + COIN_IMG.get_size()[1]):
                return True, coin

    return False, None

#def island_menu(island):
#    """ Display island menu """
#    message_display('You have arrived')


def text_objects(text, font):
    """ Generate text objects """
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def message_display(text):
    """ Display Text on screen """
    msg = pygame.font.Font('lib/fonts/MontserratAlternates-Light.ttf', 22)
    popup, popup_rect = text_objects(text, msg)
    popup_rect.center = ((DISPLAY_WIDTH*.001), (DISPLAY_HEIGHT*.001))
    GAME_DISPLAY.blit(popup, popup_rect.center)
    pygame.display.update()


def game_loop():
    """ Main game loop """
    COIN_CLOCK = 0
    ship_x = (DISPLAY_WIDTH * 0.45)
    ship_y = (DISPLAY_HEIGHT * 0.2)
    for island_name in ISLAND_NAMES:
        isle = Island(island_name,
                      random.randint(ISLAND_X_MIN, ISLAND_X_MAX),
                      random.randint(ISLAND_Y_MIN, ISLAND_Y_MAX),
                      'uninhabited')
        ISLANDS.append(isle)
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
        for i in ISLANDS:
            draw_island(i)
        for c in COINS:
            draw_coin(c)

        draw_ship(ship_x, ship_y)
        is_event, target = ship_event(ship_x, ship_y)
        if is_event:
            if target.get_type() == "island":
                message_display("You have arrived at " + target.get_name() + "!")
                if (COIN_CLOCK > 150):
                     new_coin = Coin(random.randint(COIN_X_MIN, COIN_X_MAX),
                                     random.randint(COIN_Y_MIN, COIN_Y_MAX))
                     COINS.append(new_coin)
                     COIN_CLOCK = 0

            if target.get_type() == "coin":
                COINS.remove(target)
        
        else:
            COIN_CLOCK += 1000

        COIN_CLOCK += 1
        pygame.display.update()
        CLOCK.tick(60)


game_loop()

pygame.quit()
quit()
