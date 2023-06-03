import pygame


from settings import *
def debug(*args,**kwargs):
    print(*args,**kwargs)
def image(string):
	return pygame.image.load("images/"+string)

black_square=pygame.transform.scale(image("black square.png"),(width,width))
white_square=pygame.transform.scale(image("white square.png"),(width,width))
white_highlight_square=pygame.transform.scale(image("highlight_white.png"),(width,width))
black_highlight_square=pygame.transform.scale(image("highlight_black.png"),(width,width))

def rotate_black(image):
    if ROTATE_BLACK:
        return pygame.transform.rotate(image,180)
    else:
        return image

def rotate_white(image):
    if ROTATE_WHITE:
        return pygame.transform.rotate(image,180)
    else:
        return image

bking=rotate_black(pygame.transform.scale(image("bk.svg"),(width,width)))
bqueen=rotate_black(pygame.transform.scale(image("bq.svg"),(width,width)))
brook=rotate_black(pygame.transform.scale(image("br.svg"),(width,width)))
bbishop=rotate_black(pygame.transform.scale(image("bb.svg"),(width,width)))
bknight=rotate_black(pygame.transform.scale(image("bn.svg"),(width,width)))
bpawn=rotate_black(pygame.transform.scale(image("bp.svg"),(width,width)))
#black_images=[bking,bqueen,brook,bbishop,bknight,bpawn]

wking=rotate_white(pygame.transform.scale(image("wk.svg"),(width,width)))
wqueen=rotate_white(pygame.transform.scale(image("wq.svg"),(width,width)))
wrook=rotate_white(pygame.transform.scale(image("wr.svg"),(width,width)))
wbishop=rotate_white(pygame.transform.scale(image("wb.svg"),(width,width)))
wknight=rotate_white(pygame.transform.scale(image("wn.svg"),(width,width)))
wpawn=rotate_white(pygame.transform.scale(image("wp.svg"),(width,width)))
#white_images=[wking,wqueen,wrook,wbishop,wknight,wpawn]

#if ROTATE_BLACK:
#    for image in black_images:
#        image=pygame.transform.rotate(image,180)

piece={
    "W":wpawn,
    "HW":wrook,
    "GW":wknight,
    "UW":wbishop,
    "MW":wqueen,
    "RW":wking,
     "B":bpawn,
    "HB":brook,
    "GB":bknight,
    "UB":bbishop,
    "MB":bqueen,
    "RB":bking,
}



class Box:

    def __init__(self, pos, value, color, no):
        self.pos = (pos[0] + padx, pos[1] + pady)
        self.no = no
        self.value = value
        self.width = width
        self.rootcolor = color
        self.color = color
        self.fontcolor = BLACK if self.color is WHITE else WHITE
        self.font = pygame.font.Font(pygame.font.get_default_font(), width // 2)
        self.rect = pygame.Rect(*self.pos, self.width, self.width)
        self.click = False
        self.highlight = False
        self.on_check=False
        self.click_highlight=False

        assert self.color == BLACK or self.color == WHITE, "Only black and white colors are allowed"

    def show(self, screen):
        image_color=black_square if self.color==BLACK else white_square
        if self.color==clickcolor:
        	image_color=black_highlight_square if self.rootcolor==BLACK else white_highlight_square
        screen.blit(image_color,(self.rect.topleft))
        #self.check_highlight(screen)
        #pygame.draw.rect(screen, self.color, self.rect)
        #surfObj = self.font.render(str(self.value), 1, self.fontcolor)
        if self.click:
            pygame.draw.rect(screen,(200,0,0),self.rect)
        
        if  self.on_check:
            self.check_highlight(screen)
        if self.value:
            surfObj=piece[self.value]
            #surfObj = self.font.render(str(self.no), 1, self.fontcolor)
            r=surfObj.get_rect()
            r.center=self.rect.center
            screen.blit(surfObj, r)
        # elif self.highlight:# self.color=highlightcolor
        else:
            self.color = self.rootcolor
        surfObj = self.font.render(str(self.no), 1, self.fontcolor)
        r=surfObj.get_rect()
        r.center=self.rect.center
        if DEBUG:
            screen.blit(surfObj, r)
        if self.highlight: 
            pygame.draw.circle(screen, DARK_GREEN, self.rect.center, 10)

    def clicked(self, x, y):
        return self.rect.collidepoint(x, y)
       
    def check_highlight(self,screen):
        pygame.draw.circle(screen, (200,0,0), self.rect.center, width//2)

ascii_piece={
    'H':"R",
    "G":"N",
    "U":"B",
    "M":"Q",
    "R":"K",
    "W":"P",
    "B":"p"
}

board = [
    'HW', 'GW', 'UW', 'MW', 'RW', 'UW', 'GW', 'HW',
    'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
    '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '',
    'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
    'HB', 'GB', 'UB', 'MB', 'RB', 'UB', 'GB', 'HB'
]
