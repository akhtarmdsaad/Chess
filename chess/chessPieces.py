board_no = [i for i in range(1, 65)]
color = {}
def oprint(*args,end="\n"):
    f=open("log.txt","a+")
    f.write(" ".join(list(map(str,args)))+end)
    f.close()


# MAKING CHESSBOARD
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            color[i + 1 + j * 8] = "b"
        else:
            color[i + 1 + j * 8] = "w"


def rook(pos, board):
    assert 0 < pos < 65, "pos is not accurate"
    # assert len(board[pos-1].value)==1,"Selected piece is not pawn"
    try:
        turn = board[pos - 1].value
    except:
        turn = board[pos - 1].value
    moves = []
    # up
    i = 1
    while pos - (i * 8) > 0:
        if turn[-1] in board[pos - (i * 8) - 1].value:
            break
        elif board[pos - (i * 8) - 1].value != '':  # yaani opponent ka piece hoga yaha
            moves.append(pos - (i * 8))
            break
        moves.append(pos - (i * 8))
        i += 1

    # down
    i = 1
    while pos + (i * 8) < 65:
        if turn[-1] in board[pos + (i * 8) - 1].value:
            break
        elif board[pos + (i * 8) - 1].value != '':
            moves.append(pos + (i * 8))
            break
        moves.append(pos + (i * 8))
        i += 1
    # left
    i = 1
    while pos - i > (pos - 1) // 8 * 8:
        if turn[-1] in board[pos - (i) - 1].value:
            break
        elif board[pos - (i) - 1].value != '':
            moves.append(pos - (i))
            break
        moves.append(pos - i)
        i += 1
    i = 1
    # to right
    while pos + i <= (pos + 7) // 8 * 8:
        if turn[-1] in board[pos + (i) - 1].value:
            break
        elif board[pos + i - 1].value != '':
            moves.append(pos + i)
            break
        moves.append(pos + i)
        i += 1
    return (sorted(moves))


def bishop(pos, board):
    assert 0 < pos < 65, "pos is not accurate"
    try:
        turn = board[pos - 1].value[-1]
    except:
        turn = board[pos - 1].value
    moves = []
    colour = color[pos]
    # left upper
    i = 1
    while pos - (i * 9) > 0 and colour == color[pos - (i * 9)]:
        if turn in board[pos - (i * 9) - 1].value:
            break
        elif board[pos - (i * 9) - 1].value != '':
            moves.append(pos - (i * 9))
            break
        moves.append(pos - i * 9)
        i += 1

    # right upper
    i = 1
    while pos - (i * 7) > 0 and colour == color[pos - (i * 7)]:
        if turn in board[pos - (i * 7) - 1].value:
            break
        elif board[pos - (i * 7) - 1].value != '':
            moves.append(pos - (i * 7))
            break
        moves.append(pos - i * 7)
        i += 1

    # left lower
    i = 1
    while pos + (i * 7) < 65 and colour == color[pos + (i * 7)]:
        if turn in board[pos + (i * 7) - 1].value:
            break
        elif board[pos + (i * 7) - 1].value != '':
            moves.append(pos + (i * 7))
            break
        moves.append(pos + i * 7)
        i += 1

    # right lower
    i = 1
    while pos + (i * 9) < 65 and colour == color[pos + (i * 9)]:
        if turn in board[pos + (i * 9) - 1].value:
            break
        elif board[pos + (i * 9) - 1].value != '':
            moves.append(pos + (i * 9))
            break
        moves.append(pos + i * 9)
        i += 1
    return sorted(moves)


def queen(pos, board):
    return rook(pos, board) + bishop(pos, board)


def knight(pos, board):
    moves = [pos - 17, pos - 15, pos - 10, pos - 6, pos + 6, pos + 10, pos + 15, pos + 17]
    try:
        turn = board[pos - 1].value[-1]
    except:
        turn = board[pos - 1].value
    t = []
    colour = color[pos]
    for i in moves:
        if i > 0 and i < 65 and colour != color[i]:
            t.append(i)
    i = 0
    while i != len(t):
        if turn in board[t[i] - 1].value:
            t.pop(i)
            continue
        i += 1
    return t

def castle_move(box,board,WLC,WRC,BLC,BRC):
    turn = board[box.no - 1].value[-1]
    if turn=="W":
        t=[]
        #print("Wrc:"+str(WRC),board[6].value,board[7].value,sep="\n")
        if WRC and not board[5].value and not board[6].value:
            t.append(7)
        if WLC and not board[1].value and not board[1].value and not board[4-1].value:
            t.append(3)
        return t
    elif turn=="B":
        t=[]
        if BRC and not board[61].value and not board[62].value:
            t.append(63)
        if BLC and not board[57].value and not board[58].value and not board[59].value:
            t.append(59)
        return t
    return []

def king(pos, board):
    moves = [pos - 9, pos - 8, pos - 7, pos - 1, pos + 1, pos + 7, pos + 8, pos + 9]
    try:
        turn = board[pos - 1].value[-1]
    except:
        turn = board[pos - 1].value
    
    if pos % 8 == 0:
        moves.remove(pos - 7)
        moves.remove(pos + 1)
        moves.remove(pos + 9)
    elif pos % 8 == 1:
        moves.remove(pos - 9)
        moves.remove(pos - 1)
        moves.remove(pos + 7)
    t = moves
    i = 0
    print(t)
    while i != len(t):
        j = t[i]
        
        print(board[j-1].value)
        if j < 0 or j > 65:
            t.pop(i)
            continue
        try:
            if turn in board[j - 1].value:
                t.pop(i)
                continue
        except Exception as e:
            raise
            print(e)
        
        i += 1
    # Castling the king and rook

    # if king_is_not_moved and no check then
    # if rook not moved and inbetween them nothing is present
    # king.pos += 2 and rook.pos = king.pos-1
    print(t)
    return t


def pawn(pos, board):
    # assuming white pawn is up
    try:
        turn = board[pos - 1].value[-1]
    except:
        turn = board[pos - 1].value
    if turn == 'W':
        if (pos // 8 == 1 or pos == 16) and board[pos + 16 - 1].value == "":  # first  chaal 2 step,
            if board[pos + 8 - 1].value:
                t=[]
            else:
                t = [pos + 8, pos + 16]
        elif board[pos + 8 - 1].value == "":
            t = [pos + 8]
        else:
            t = []
        try:
            if "B" in board[pos + 9 - 1].value:
                t.append(pos + 9)
        except:pass
        try:
            if "B" in board[pos + 7 - 1].value:
                t.append(pos + 7)
        
        except:pass

    elif turn == 'B':
        if (pos // 8 == 6 or pos == 56) and pos!=48 and board[pos - 16 - 1].value == "":
            if board[pos - 8 - 1].value:
                t=[]
            else:
                t = [pos - 8, pos - 16]
        elif board[pos - 8 - 1].value == "":
            t = [pos - 8]
        else:
            t = []
        if "W" in board[pos - 9 - 1].value:
            t.append(pos - 9)
        if "W" in board[pos - 7 - 1].value:
            t.append(pos - 7)

    else:
        t = []
    return t
