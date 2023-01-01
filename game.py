from minmax import minmax
import time
import pygame as pg
class board():
    def __init__(self):
        self.board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

    def print_board(self):
        print("\n_____________\n")
        for row in self.board:
            print('| ', end = '')
            for i in row:
                print(i, end=' |')
            print("\n_____________\n")

    def make_move(self, player, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        else:
            print("That spot is already taken!")
            return False

    def check_win(self):
        for i in range(3):
            #Check columns
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            #Check rows
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        #Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        else:
            return False

    def check_tie(self):
        tie = True
        for row in self.board:
            for pos in row:
                if pos == ' ':
                    return False
        if(tie and not self.check_win()):
            return True

    def evaluate(self, depth):
        score = 0
        w = self.check_win()
        if w == 'X':
            score += (10 - depth)
        elif w == 'O':
            score -= (10 - depth)
        
        return score


    def makeAIMove(self, newBoard):
        self.board = newBoard.board
        return


b = board()
pg.init()
screen = pg.display.set_mode((600, 600))
pg.display.set_caption("Tic Tac Toe")
clock = pg.time.Clock()
running = True
while running:
    clock.tick(60)
    if b.check_win():
        print("Player {} wins!".format(b.check_win()))
        time.sleep(3)
        running = False
    elif b.check_tie():
        print("Tie game!")
        time.sleep(3)
        running = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if event.type == pg.MOUSEBUTTONDOWN:
        pos = pg.mouse.get_pos()
        i = pos[0]//200
        j = pos[1]//200
        if b.board[i][j] == ' ':
            b.make_move('O', i, j)
            value, newBoard = minmax(b, 6, True)
            b.makeAIMove(newBoard)

    screen.fill((255, 255, 255))
    #draw the board
    pg.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 5)
    pg.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 5)
    pg.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), 5)
    pg.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 5)
    
    #draw x's and o's from the board
    for i in range(3):
        for j in range(3):
            if b.board[i][j] == 'X':
                pg.draw.line(screen, (0, 0, 0), (i*200+10, j*200+10), (i*200+190, j*200+190), 5)
                pg.draw.line(screen, (0, 0, 0), (i*200+190, j*200+10), (i*200+10, j*200+190), 5)
            elif b.board[i][j] == 'O':
                pg.draw.circle(screen, (0, 0, 0), (i*200+100, j*200+100), 90, 5)

    pg.display.flip()
pg.quit()

