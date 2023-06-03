import pygame
import sys
from pygame.locals import *
import pickle
from chessPieces import *
from players import *
from settings import *
#import chess
import starting
gameplay=starting.main()
pygame.init()
filename="game.pkl"
f=open("log.txt","w+")
f.truncate()
f.close()
def oprint(*args,end="\n"):
    f=open("log.txt","a+")
    f.write(" ".join(list(map(str,args)))+end)
    f.close()

def save_game():
    global boards
    #boards.append([[box.value for box in boxes],turn,WLC,WRC,BLC,BRC])
    pickle.dump(boards,open(filename,"wb"),3)

def load_game():
    return pickle.load(open(filename,"rb"))

screen = pygame.display.set_mode((500, 500))
highlight_boxes = []
boxes = []
box_selected = None
box_selected_2 = None
#Castle
global WLC,WRC,BLC,BRC
BLC=BRC=WLC=WRC=True

if WHITE_DOWN:
    for j in range(8):
        for i in range(8):
            boxes.append(Box((width * (7-i), width * (7-j)), 0, BLACK if (i + j) % 2 == 0 else WHITE, i + 1 + j * 8))
else:
    for j in range(8):
        for i in range(8):
            boxes.append(Box((width * i, width * j), 0, BLACK if (i + j) % 2 == 0 else WHITE, i + 1 + j * 8))



#print([box.no for box in boxes])
for i in range(len(board)):
    boxes[i].value = board[i]

def boxes_to_board(turn):
    fen=""
    for i,box in enumerate(boxes):
        if (i+1)%8==0:
            fen+="/"
        p=box.value
        if p:
            pass
        else:
            if "W" in p:
                fen+=ascii_piece[p.strip("WB")].upper()
            else:
                fen+=ascii_piece[p.strip("WB")].lower()
            
    return fen
            

def check_checkmate(turn):
    return
    ascii_board=chess.Board(boxes_to_board(turn))
    


def check(turn):
    turn=turn.upper()
    king_box=None
    if "B" in turn:
        opponent_piece_boxes=[box for box in boxes if "W" in box.value]
        for box in boxes:
            if "RB" in box.value:
                king_box=box
                break
    elif "W" in turn:
        opponent_piece_boxes=[box for box in boxes if "B" in box.value]
        for box in boxes:
            if "RW" in box.value:
                king_box=box
                break
    if not king_box:
        return None
    for box in opponent_piece_boxes:
        for move_box in moves_allowed(box):
            if move_box==king_box.no:
                king_box.on_check=True
                return True
    return False

def which_castle_move(bs,bs2):
    if not "R" in bs.value:
        return None
    else:
        if bs.no==5:
            if bs2.no == 3:
                return "wlc"
            elif bs2.no==7:
                return "wrc"
        if bs.no==61:
            if bs2.no==59:
                return "blc"
            elif bs2.no==63:
                return "brc"
    return None
def moves_allowed(box):
    #return all possible moves of that box piece
    if not box:
        return []
    piece = box.value
    if "H" in piece:
        return rook(box.no, boxes)
    elif "U" in piece:
        return bishop(box.no, boxes)
    elif "M" in piece:
        return queen(box.no, boxes)
    elif "G" in piece:
        return knight(box.no, boxes)
    elif "R" in piece:        
        a=king(box.no, boxes)
        
        b=castle_move(box,boxes,WLC,WRC,BLC,BRC)
        return a+b
    elif len(piece) == 1:
        # its pawn
        return pawn(box.no, boxes)
    return []
font=pygame.font.Font(pygame.font.get_default_font(), 100)
surf=font.render("UNDO",1,(255,255,255))
undo_rect=surf.get_rect()
undo_rect.center=(300,1100)

boards = []
previous_moved_boxes=[]

def highlight(boxes_no):
    global boxes
    for no in boxes_no:
        for box in boxes:
            if box.no == no:
                box.highlight = True
    global highlight_boxes
    highlight_boxes = boxes_no
    return boxes_no

def no_to_box(no_list):
    t=[]
    global boxes
    for box in boxes:
        if box.no in no_list:
            t.append(box)
    return t

number = 1

def queen_respawn(box):
        if box.no > 56 and box.value=="W":
            box.value="MW"
        if box.no < 9 and box.value=="B":
            box.value="MB"

control_pressed = False
boards.append([[box.value for box in boxes],turn,WLC,WRC,BLC,BRC])
if gameplay=="load":
    boards=load_game()
    undo_boxes = boards.pop()
    undoing_boxes=undo_boxes.pop(0)
    turn=undo_boxes.pop(0)
    print(undo_boxes)
    #global WLC,WRC,BLC,BRC
    WLC,WRC,BLC,BRC=undo_boxes

    for box,value in zip(boxes,undoing_boxes):
        box.value=value

while True:
    try:
        screen.fill((bgcolor))
        screen.blit(surf,undo_rect)
        for box in previous_moved_boxes:
            box.color=clickcolor
        # draw boxes
        pygame.draw.rect(screen, BLACK, (padx, pady, 8 * width, 8 * width), 5)
        
        for box in boxes:
            box.show(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_LCTRL or event.key == K_RCTRL:
                    control_pressed = True
                if control_pressed and event.key == K_z:
                    undo_boxes = boards.pop()
                    turn=undo_boxes.pop()
                    print([b.value for b in undo_boxes])

                    boxes = undo_boxes
                    print("undo")
            if event.type == KEYUP:
                if event.key == K_LCTRL or event.key == K_RCTRL:
                    control_pressed = False
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if undo_rect.collidepoint(event.pos):
                    undo_boxes = boards.pop()
                    undoing_boxes=undo_boxes.pop(0)
                    turn=undo_boxes.pop(0)
                    #global WLC,WRC,BLC,BRC
                    WLC,WRC,BLC,BRC=undo_boxes

                    for box,value in zip(boxes,undoing_boxes):
                        box.value=value
                    print("undo")
                    
                if box_selected:
                    
                    # get clicked box
                    for box in boxes:
                        if box.clicked(x, y):
                            box_selected_2 = box
                            break
                    if not box_selected_2:
                        continue

                    # check if box in highlight_boxes
                    if box_selected_2.highlight:
                        if turn == "W":
                            boards.append([[box.value for box in boxes],turn,WLC,WRC,BLC,BRC])
                            turn="B"
                            x = [b.value for b in boxes]
                            if "RW" in box_selected.value:
                                #global WLC,WRC
                                WLC=WRC=False
                            elif "HW" in box_selected.value:
                                #global WLC,WRC
                                if box_selected.no==8:
                                    WRC=False
                                elif box_selected.no==1:
                                    WLC=False
                            if "RB" not in x:
                                print("White Won")
                                exit(0)
                        else:
                            boards.append([[box.value for box in boxes],turn,WLC,WRC,BLC,BRC])
                            turn = "W"
                            x = [b.value for b in boxes]
                            if "RB" in box_selected.value:
                                #global BLC,BRC
                                BLC=BRC=False
                            elif "HB" in box_selected.value:
                                #global BLC,BRC
                                if box_selected.no==57:
                                    BLC=False
                                elif box_selected.no==64:
                                    BRC=False
                            if "RW" not in x:
                                print("Black Won")
                                exit(0)
                               
                        box_selected_2.value = box_selected.value
                        previous_moved_boxes=[box_selected,box_selected_2]
                        c=which_castle_move(box_selected,box_selected_2)
                        queen_respawn(box_selected_2)
                        
                        box_selected.value = ""
                        if c:    #special for rook move in castle
                            #global BLC,BRC,WLC,WRC
                            if c=="wlc":
                                boxes[3].value=boxes[0].value
                                boxes[0].value=""
                                WLC=WRC=False
                            elif c=="wrc":
                                boxes[5].value=boxes[7].value
                                boxes[7].value=""
                                WLC=WRC=False
                            elif c=="blc":
                                boxes[59].value=boxes[56].value
                                boxes[56].value=""
                                BLC=BRC=False
                            elif c=="brc":
                                boxes[61].value=boxes[63].value
                                boxes[63].value=""
                                BLC=BRC=False
                            print(WLC,WRC,BLC,BRC)
                       # for b in boxes:
                      #      b.on_check=False
                        #if check(turn):
#                            print("Check")
#                            check_checkmate(turn)
                        save_game()

                    box_selected = None
                    box_selected_2 = None
                    for b in boxes:
                        b.click = False
                        b.highlight = False
                        b.color=b.rootcolor
            
                else:
                    
                    # to click boxes
                    for box in boxes:
                        box.click=False
                        if box.clicked(x, y):
                            box_selected = box
                            box_selected.click = not box_selected.click
                            break
                    print(box_selected.value)
                    
                    try:
                        if box_selected.value[-1] != turn:
                            box_selected = None
                            continue
                    except:
                        #print(box_selected.value)
                        raise
                    try:
                        number = box_selected.no
                    except:
                        raise
                    #print(box_selected.value)
                    if "R" not in box_selected.value:
                        highlight(moves_allowed(box_selected))
                    else:
                        highlight([box.no for box in boxes])
                    

        pygame.display.update()
    except Exception as e:
        print(e)
        #raise
        if DEBUG:
            raise
        
        
        
