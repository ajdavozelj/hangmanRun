import pygame
import requests
import dotenv
import os


API_KEY = os.getenv("API_KEY")
Navodila = "tell me random english word on B1 level and without explanation or any other text or signs (so no *) "
def pogovor_z_llm():
    url = "https://api.llm7.io/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "default",
        "messages": [
            {"role": "user", "content":Navodila}
        ]
    }
    response =requests.post(url, headers=headers, json=data)
    #print(response.json())
    print(response.json()["choices"][0]["message"]["content"])

dotenv.load_dotenv()
pogovor_z_llm()




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