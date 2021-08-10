import pygame, sys
import numpy as np

# We should always initialize pygame before using it

pygame.init()

# creating screen
#constant here-
#board coordinates
WIDTH= 600
HEIGHT= WIDTH
LINE_WIDTH= 10
RED = (255,0,0) #RGB color format
BLACK= (0,0,0)
WHITE= (255,255,255)
#BG_C= (20,170,146)
BG_C= (203,195,227)
LINE_C= (150,150,150)
BOARD_ROWS=3
BOARD_COLS=3
SQUARE= WIDTH//BOARD_COLS
CIRCLE_R= SQUARE//3 #to get dynamic size acc to screen
CIRCLE_WIDTH=10
SPACE= SQUARE//4
screen= pygame.display.set_mode((WIDTH,HEIGHT))     #initialize width & height
#customizing screen
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_C) #create colours

#console board create
board=np.zeros((BOARD_ROWS,BOARD_COLS))


#function which creates lines for board
def draw_board():
    # create a line btw two points
    # 1st H line
    pygame.draw.line(screen,LINE_C,(0,SQUARE),(WIDTH,SQUARE),LINE_WIDTH)
    #2nd H line
    pygame.draw.line(screen,LINE_C,(0,2*SQUARE),(WIDTH,2*SQUARE),LINE_WIDTH)
    #1st V line
    pygame.draw.line(screen, LINE_C, (SQUARE, 0), (SQUARE, HEIGHT), LINE_WIDTH)
    #2nd V line
    pygame.draw.line(screen, LINE_C, (2*SQUARE,0), (2*SQUARE,HEIGHT), LINE_WIDTH)

#player marking on board
def mark_square(row,col,player):
    board[row][col]= player

#returns availability of square
def available_square(row,col):
    return board[row][col]==0

# check full board
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==0:
                return False
    return True

#draw figures
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                # center for circle
                pygame.draw.circle(screen, WHITE, (int(col * SQUARE + (SQUARE/2)),int(row*SQUARE + (SQUARE/2))),
                                   CIRCLE_R,CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, BLACK, (col*SQUARE+SPACE,row*SQUARE+SQUARE-SPACE), (col*SQUARE+SQUARE-SPACE,row*SQUARE+SPACE), 20)
                pygame.draw.line(screen, BLACK, (col * SQUARE+SPACE, row * SQUARE+SPACE), (col * SQUARE + SQUARE-SPACE, row * SQUARE + SQUARE-SPACE), 20)


#check for win
def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            vertical_line(player,col)
            return True
    # horizontal win
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            horizontal_line(player,row)
            return True
    #diagonal win- ascending
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        asc_diagonal_line(player)
        return True
    #diagonal win- descending
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        des_diagonal_line(player)
        return True

    return False

# draw vertical winning line
def vertical_line(player,col):
    posX= col*SQUARE+(SQUARE/2)
    if player==1:
        color=WHITE
    elif player==2:
        color=BLACK
    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)

# draw horizontal winning line
def horizontal_line(player,row):
    posY = row * SQUARE + (SQUARE / 2)
    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK
    pygame.draw.line(screen, color, (15, posY), (WIDTH-15,posY), 15)

# draw ascending diagonal winning line
def asc_diagonal_line(player):
    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK
    pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH-15,15), 15)

#draw descending diagonal winning line
def des_diagonal_line(player):
    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK
    pygame.draw.line(screen, color, (15, 15), (HEIGHT -15,WIDTH-15), 15)

#restart game
def restart():
    screen.fill(BG_C)
    draw_board()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col]=0

draw_board()

player=1
game_over=False
# we need to create a main loop always
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()      # exit the screen on quit red button
        #link console board to screen board
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX= event.pos[0] #x coordinate
            mouseY= event.pos[1] #y coordinate
            #map mouseX & mouseY bcause they are between 0-600(image size)
            click_row= int(mouseY//SQUARE)
            click_col= int(mouseX//SQUARE)

            # fill board with alternative player
            if available_square(click_row,click_col):
                mark_square(click_row, click_col, player)
                if check_win(player):
                    game_over = True
                player= player%2 +1  #switch btw 1 and 2
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                player = 1
                game_over = False
                restart()

    pygame.display.update() #update screen for displaying customs


