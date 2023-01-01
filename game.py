from minmax import minmax

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

    def evaluate(self):
        score = 0
        w = self.check_win()
        if w == 'X':
            score += 10
        elif w == 'O':
            score -= 10

        else:
            #check for 2 in a line
            for i in range(3):
                #Check columns
                if self.board[i][0] == self.board[i][1] != ' ':
                    if self.board[i][0] == 'X':
                        score += 3
                    else:
                        score -= 3
                if self.board[i][1] == self.board[i][2] != ' ':
                    if self.board[i][1] == 'X':
                        score += 3
                    else:
                        score -= 3
                #Check rows
                if self.board[0][i] == self.board[1][i] != ' ':
                    if self.board[0][i] == 'X':
                        score += 3
                    else:
                        score -= 3
                if self.board[1][i] == self.board[2][i] != ' ':
                    if self.board[1][i] == 'X':
                        score += 3
                    else:
                        score -= 3
            #Check diagonals
            if self.board[0][0] == self.board[1][1] != ' ': 
                if self.board[0][0] == 'X':
                    score += 3
                else:
                    score -= 3
            if self.board[1][1] == self.board[2][2] != ' ': 
                if self.board[1][1] == 'X':
                    score += 3
                else:
                    score -= 3
            if self.board[0][2] == self.board[1][1] != ' ':
                if self.board[0][2] == 'X':
                    score += 3
                else:
                    score -= 3
            if self.board[1][1] == self.board[2][0] != ' ':
                if self.board[1][1] == 'X':
                    score += 3
                else:
                    score -= 3
        return score

    def makeAIMove(self, newBoard):
        self.board = newBoard.board
        return



b = board()
b.print_board()
player = 'O'
position = [0,1,2]
while(not(b.check_win() or b.check_tie())):
    if(player == 'O'):
        moved = False
        while(not moved):
            row = int(input("Row: "))
            col = int(input("Col: "))
            if(row in position and col in position):
                moved = b.make_move(player, row, col)
            else:
                print("Invalid input")
                moved = False
        player = 'X'
    else:
        value, newBoard = minmax(b, 5, True)
        b.makeAIMove(newBoard)
        player = 'O'

    b.print_board()

if b.check_win():
    print("Player {} wins!".format(b.check_win()))
else:
    print("Tie game!")


