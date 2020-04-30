numTiles = 10

board = [1,
        1,  1,
        1,  1,  1,
        1,  1,  1,  1]

moves = [[0,1,3],[0,2,5],[1,4,8],[1,3,6],[2,5,9],[2,4,7],[3,4,5],[3,1,0],[5,2,0],[4,5,3],[6,7,8],[6,3,1],[7,8,9],[7,4,2],[8,7,6],[8,4,1],[9,8,7],[9,5,2]]
pastMoves = []
finishedGames = []

def makeAMove(board, pastMoves):
    global moves, finishedGames
    if(len(pastMoves) != 8):
        for move in moves:
            if(board[move[0]] == 1 and board[move[1]] == 1 and board[move[2]] == 0):
                pM = pastMoves.copy()
                pM.append(move)

                nB = board.copy()
                nB[move[0]] = 0
                nB[move[2]] = 1
                nB[move[1]] = 0
                makeAMove(nB, pM)
    else:
        finishedGames.append(pastMoves)

for i in range(10):
    bc = board.copy()
    bc[i] = 0
    pastMoves = []
    makeAMove(bc, pastMoves)

for game in finishedGames:
    gameMoves = 0
    for moveNumber in range(len(game)-1):
        if(game[moveNumber][2] != game[moveNumber+1][0]):
            gameMoves = gameMoves + 1;

    if(gameMoves <5):
        print(game)
        print(gameMoves)