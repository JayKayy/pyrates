import pygame
import os
import sys


pygame.init()

display_width = 600
display_height = 800

black = (0,0,0)
white = (255, 255, 255)
ocean = (60,24,19)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Evan\'s Game')
clock = pygame.time.Clock()

shipImg = pygame.image.load('ship.png')
x_min = 0
x_max = (display_width - shipImg.get_size()[0])
y_min = 0
y_max = (display_height - shipImg.get_size()[1])

def ship(x,y):
    if x < x_min:
        x = x_min
    if x > x_max:
        x = x_max
    if y < y_min:
        y = y_min
    if y > y_max:
        y = y_max
    gameDisplay.blit(shipImg, (x,y))

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.2)

    x_change = 0
    y_change = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed =  True
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
    
        x += x_change 
        y += y_change
    
        gameDisplay.fill(white)
        ship(x,y)
    
        pygame.display.update()
        clock.tick(60)

game_loop()

pygame.quit()
quit()


