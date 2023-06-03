import pygame
def image(string):
	return pygame.image.load("images/"+string)

background=image("landscape.jpg")
background=pygame.transform.scale(background,(3840,2138))
pygame.init()
font=pygame.font.Font(pygame.font.get_default_font(),50)
surf_load=font.render("Load Game",1,(0,0,0))
play_rect=surf_load.get_rect()
play_rect.center=(300,300)
surf_new=font.render("Play new Game",1,(0,0,0))
play_new_rect=surf_new.get_rect()
play_new_rect.center=(300,200)
#background=pygame.transform.rotate(background,-90)
