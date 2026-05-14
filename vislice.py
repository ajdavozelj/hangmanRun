import pygame
import requests
import dotenv
import os

pygame.init()

canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Vislice")

color = (0, 0, 0)


exit = False

while not exit:
	canvas.fill(color)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True


	pygame.display.update()