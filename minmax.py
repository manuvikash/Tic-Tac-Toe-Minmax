from copy import deepcopy

def minmax(board, depth, max_player):
    if(depth == 0 or board.check_win() or board.check_tie()):
        return board.evaluate(depth), board

    if(max_player):
        maxEval = float('-inf')
        bestMove = None
        for move in getAllMoves(board, 'X'):
            evaluation = minmax(move, depth-1, False)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                bestMove = move
        
        return maxEval, bestMove

    else:
        minEval = float('inf')
        bestMove = None
        for move in getAllMoves(board, 'O'):
            evaluation = minmax(move, depth-1, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                bestMove = move

        return minEval, bestMove

def getAllMoves(position, player):
    moves = []
    for i in range(3):
        for j in range(3):
            if(position.board[i][j] == ' '):
                temp_pos = deepcopy(position)
                temp_pos.make_move(player, i, j)
                moves.append(temp_pos)

    return moves