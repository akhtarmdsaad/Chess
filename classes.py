import pygame
def image(string):
	return pygame.image.load("images/"+string)

background=image("landscape.jpg")
background=pygame.transform.scale(background,(3840,2138))
pygame.init()
font=pygame.font.Font(pygame.font.get_default_font(),50)
surf=font.render("PlayGame",1,(200,200,200))
play_rect=surf.get_rect()
play_rect.center=(300,200)

#background=pygame.transform.rotate(background,-90)
