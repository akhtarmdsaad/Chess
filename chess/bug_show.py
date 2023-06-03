import pygame
from pygame.locals import *
import pickle
from chessPieces import *
from players import *
from settings import *
pygame.init()
filename="game.pkl"

def load_game():
    return pickle.load(open(filename,"rb"))

screen = pygame.display.set_mode((500, 500))
pointer=0

boxes=[]
if WHITE_DOWN:
    for j in range(8):
        for i in range(8):
            boxes.append(Box((width * (7-i), width * (7-j)), 0, BLACK if (i + j) % 2 == 0 else WHITE, i + 1 + j * 8))
else:
    for j in range(8):
        for i in range(8):
            boxes.append(Box((width * i, width * j), 0, BLACK if (i + j) % 2 == 0 else WHITE, i + 1 + j * 8))
font=pygame.font.Font(pygame.font.get_default_font(), 100)
fontO=pygame.font.Font(pygame.font.get_default_font(), 20)

#left arrow
las=font.render("<",1,(255,255,255))
lar=las.get_rect()
lar.center=(200,800)

#right arrow
ras=font.render(">",1,(255,255,255))
rar=ras.get_rect()
rar.center=(500,800)


#full left
lla=font.render("<--",1,(255,255,255))
llar=lla.get_rect()
llar.center=(50,800)

#full right
rra=font.render("-->",1,(255,255,255))
rrar=rra.get_rect()
rrar.center=(650,800)

if True:
    boards=load_game()
    undo_boxes = boards.pop()
    undoing_boxes=undo_boxes.pop(0)
    args=undo_boxes
    turn=undo_boxes.pop(0)
    print(undo_boxes)
    #global WLC,WRC,BLC,BRC
    WLC,WRC,BLC,BRC=undo_boxes
    
    for box,value in zip(boxes,undoing_boxes):
        box.value=value
def show_text(pos,*args):
    for a in args:
        surf=fontO.render(str(a),1,(255,255,255))
        screen.blit(surf,pos)
while True:
    screen.fill((0,0,0))
    
    for box in boxes:
        box.show(screen)
    screen.blit(las,lar)
    screen.blit(ras,rar)
    screen.blit(lla,llar)
    screen.blit(rra,rrar)
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            if lar.collidepoint(event.pos):
                if pointer>0:
                    pointer-=1
            if rar.collidepoint(event.pos):
                if pointer<len(boards)-1:
                    pointer+=1
            if llar.collidepoint(event.pos):
                pointer=0
            if rrar.collidepoint(event.pos):
                pointer=len(boards)-1
            b=boards[pointer]
            args=b[1:]
            for box,value in zip(boxes,b[0]):
                box.value=value
    
    show_text((100,900),args)
    pygame.display.update()