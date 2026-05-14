import pygame
import requests
import dotenv
import os

pygame.init()
pygame.mixer.init()
ozadje = pygame.image.load("dungeon.jpg")
ozadje = pygame.transform.scale(ozadje, (800, 800))
monster = image.load("monster3.png")
#monster =  pygame.transform.scale(monster, (,))
hero = pygame.image.load("hero.png")
#hero =  pygame.transform.scale(hero, (,))
hero_back = pygame.image.load("hero_back.png")
#hero_back =  pygame.transform.scale(hero_back, (,))
canvas = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Vislice")

color = (0, 0, 0)


exit = False

while not exit:
	canvas.blit(ozadje, (0, 0))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True


	pygame.display.update()