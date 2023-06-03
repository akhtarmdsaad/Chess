import pygame,sys,math
from pygame.locals import *
from classes import *

def main():
    pygame.init()
    screen=pygame.display.set_mode((500,500))
    screenX,screenY=screen.get_size()
    win_rect=screen.get_rect()
    window_center_x,window_center_y=win_rect.center
    
    ofx=ofy=0
    
    back_rect=background.get_rect()
    
    play=True
    pygame.mouse.set_pos((720,720))
    while play:
    	screen.fill((255,255,255))
    	screen.blit(background,(ofx,ofy))
    	screen.blit(surf_load,play_rect)
    	screen.blit(surf_new,play_new_rect)
    	
    	for event in pygame.event.get():
    		if event.type==QUIT:
    			pygame.quit()
    			sys.exit(0)
    		if event.type==MOUSEBUTTONDOWN:
    			x,y=event.pos
    			#print(play_rect,x)
    			if play_rect.collidepoint(x,y):
    				return "load"
    			if play_new_rect.collidepoint(x,y):
    				return "new"
    	##pygame.draw.rect(screen,(0,0,0),play_rect)
    	if True or pygame.mouse.get_pressed()[0]:
    		x,y=pygame.mouse.get_pos()
    		dx=window_center_x-x
    		dy=window_center_y-y
    		ofx+=math.copysign(abs(dx//100),dx)
    		ofy+=math.copysign(abs(dy//100),dy)
    		if ofx>0:
    			ofx=0
    		elif ofx<720-back_rect.right:
    			ofx=720-back_rect.right
    		if ofy>0:
    			ofy=0
    		elif ofy<1344-back_rect.bottom:
    			ofy=1344-back_rect.bottom
    		#background.scroll(dx=int(dx),dy=int(dy))
    		
    	pygame.display.update()
if __name__=="__main__":
    main()