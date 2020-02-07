from colorama import init, Fore, Back, Style
from copy import deepcopy
import math

fieldSizeX = 5
fieldSizeY = 2
fieldEmpty = " "
previewMarker = "."
# [Dark Field Color, Light Field Color]
previewBackColors = [Back.YELLOW, Back.LIGHTYELLOW_EX]
normalBackColors = [Back.BLACK, Back.WHITE]
whitePlayerColor = Fore.LIGHTWHITE_EX
blackPlayerColor = Fore.RED
borderColor = Back.GREEN + Fore.LIGHTYELLOW_EX

def showBoard(board):
    printableBoard = []
    for i, line in enumerate(board):
        for k in range(fieldSizeY):
            printableLine = []
            for j, field in enumerate(line):
                printableField = []
                backColor = ""
                if previewMarker in field:
                    backColor = previewBackColors[(i + j) % 2]
                    field = field.replace(previewMarker, "")
                else:
                    backColor = normalBackColors[(i + j) % 2]
                printableField.extend([(backColor  + fieldEmpty) for i in range(fieldSizeX)])
                if k == fieldSizeY // 2:
                    printableField[fieldSizeX // 2] = backColor + field
                printableLine.append(printableField)
            printableBoard.append(printableLine)

    print(borderColor, "   ", " " * (fieldSizeX // 2), sep = "", end = Style.RESET_ALL)
    for i in range(7):
        print(borderColor, chr(ord("A") + i) + " " * (fieldSizeX - 1), sep = "", end = Style.RESET_ALL)
    print(borderColor, "H", " " * (fieldSizeX // 2 - 1), "   ", sep = "", end = Style.RESET_ALL)
    print("")
    for i in range(len(printableBoard)):
        print(borderColor, end = "")
        if (i + fieldSizeY // 2 + 1) % fieldSizeY == 0:
            print(" ", (len(printableBoard) - i - 1) // fieldSizeY + 1, " ", sep = "", end = "")
        else:
            print("   ", end = "")
        print(Style.RESET_ALL, end = "")

        for field in printableBoard[len(printableBoard) - 1 - i]:
            print("".join(field), end = "")
        print(Style.RESET_ALL, end = "")

        if (i + fieldSizeY // 2 + 1) % fieldSizeY == 0:
            print(borderColor, " ", (len(printableBoard) - i - 1) // fieldSizeY + 1, " ", Style.RESET_ALL, sep = "")
        else:
            print(borderColor, "   ", Style.RESET_ALL, sep = "")
        print(Style.RESET_ALL, end="")
    print(borderColor, "   ", " " * (fieldSizeX // 2), sep = "", end="")
    for i in range(7):
        print(borderColor, chr(ord("A") + i) + " " * (fieldSizeX - 1), sep = "", end = Style.RESET_ALL)
    print(borderColor, "H", " " * (fieldSizeX // 2 - 1), "   ", sep = "", end = Style.RESET_ALL)
    print(" ", Style.RESET_ALL, sep = "")
    print("")

def newBoard():
    b = [[fieldEmpty for i in range(8)] for i in range(8)]
    figs = ["R", "N", "B", "Q", "K", "B", "N", "R"]
    for i in range(8):
        b[0][i] = whitePlayerColor + figs[i] + Style.RESET_ALL
        b[1][i] = whitePlayerColor + "P"     + Style.RESET_ALL
        b[6][i] = blackPlayerColor + "P"     + Style.RESET_ALL
        b[7][i] = blackPlayerColor + figs[i] + Style.RESET_ALL
    return b

def fieldInBoard(x, y):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return False
    else:
        return True

def noPreviewMarkers(board):
    for i, line in enumerate(board):
        for j, field in enumerate(line):
            board[i][j] = field.replace(previewMarker, "")

def quantumMove(board, xFrom, yFrom, xTo = -1, yTo = -1, preview = False):
    piece = board[yFrom][xFrom]
    newPositions = []
    pieceColor = ""
    if whitePlayerColor in piece:
        pieceColor = whitePlayerColor
    elif blackPlayerColor in piece:
        pieceColor = blackPlayerColor

    noPreviewMarkers(board)

    if "P" in piece:
        if pieceColor == whitePlayerColor:
            if yFrom < 7:
                if board[yFrom + 1][xFrom] == fieldEmpty:
                    newPositions.append([yFrom + 1, xFrom])
                if yFrom == 1 and board[3][xFrom] == fieldEmpty:
                    newPositions.append([3, xFrom])
                if xFrom > 0:
                    if blackPlayerColor in board[yFrom + 1][xFrom - 1]:
                        newPositions.append([yFrom + 1, xFrom - 1])
                if xFrom < 7:
                    if blackPlayerColor in board[yFrom + 1][xFrom + 1]:
                        newPositions.append([yFrom + 1, xFrom + 1])
        elif pieceColor == blackPlayerColor:
            if yFrom > 0:
                if board[yFrom - 1][xFrom] == fieldEmpty:
                    newPositions.append([yFrom - 1, xFrom])
                if yFrom == 6 and board[4][xFrom] == fieldEmpty:
                    newPositions.append([4, xFrom])
                if xFrom > 0:
                    if whitePlayerColor in board[yFrom - 1][xFrom - 1]:
                        newPositions.append([yFrom - 1, xFrom - 1])
                if xFrom < 7:
                    if whitePlayerColor in board[yFrom - 1][xFrom + 1]:
                        newPositions.append([yFrom - 1, xFrom + 1])
    elif "N" in piece:
        moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        for move in moves:
            nextX = xFrom + move[0]
            nextY = yFrom + move[1]
            if fieldInBoard(nextX, nextY):
                if board[nextY][nextX] == fieldEmpty or pieceColor not in board[nextY][nextX]:
                    newPositions.append([nextY, nextX])

    elif "B" in piece or "R" in piece or "Q" in piece:
        moves = []
        if "B" in piece or "Q" in piece:
            moves.extend([[1, 1], [-1, 1], [1, -1], [-1, -1]])
        if "R" in piece or "Q" in piece:
            moves.extend([[0, 1], [0, -1], [1, 0], [-1, 0]])

        for move in moves:
            cont = True
            nextX = xFrom
            nextY = yFrom
            while cont:
                nextX += move[0]
                nextY += move[1]
                cont = False
                if fieldInBoard(nextX, nextY):
                    if board[nextY][nextX] == fieldEmpty:
                        newPositions.append([nextY, nextX])
                        cont = True
                    elif pieceColor not in board[nextY][nextX]:
                        newPositions.append([nextY, nextX])

    elif "K" in piece:
        moves = [[0, 1], [0, -1], [1, 1], [1, 0], [1, -1], [-1, 1], [-1, 0], [-1, -1]]
        possibleMoves = []
        for move in moves:
            nextX = xFrom + move[0]
            nextY = yFrom + move[1]
            if fieldInBoard(nextX, nextY):
                if board[nextY][nextX] == fieldEmpty or pieceColor not in board[nextY][nextX]:
                    if preview:
                        newPositions.append([nextY, nextX])
                    else:
                        possibleMoves.append([nextY, nextX])
        if not preview:
            if [yTo, xTo] in possibleMoves:
                newPositions.append([yTo, xTo])
            elif len(possibleMoves) == 1:
                newPositions.append(possibleMoves[0])

    check = False
    if newPositions:
        for position in newPositions:
            if preview:
                board[position[0]][position[1]] += previewMarker
                if "K" in board[position[0]][position[1]]:
                    check = True
            else:
                board[position[0]][position[1]] = piece
        if not preview:
            board[yFrom][xFrom] = fieldEmpty

    return check

def check(board, player):
    opponent = whitePlayerColor
    if player == whitePlayerColor:
        opponent = blackPlayerColor
    for i in range(8):
        for j in range(8):
            if opponent in board[j][i]:
                if quantumMove(board, i, j, -1, -1, True):
                    return True
    return False

def checkmate(board, player):
    mate = True
    noMateMoves = []
    opponent = whitePlayerColor
    if player == whitePlayerColor:
        opponent = blackPlayerColor
    testBoard = deepcopy(board)

    if check(testBoard, player):
        for i in range(8):
            for j in range(8):
                if player in board[j][i]:
                    moveRange = [0]
                    if "K" in board[j][i]:
                        moveRange = [-1, 0, 1]
                    for ii in moveRange:
                        for jj in moveRange:
                            quantumMove(testBoard, i, j, i+ii, j+jj)
                            if not check(testBoard, player):
                                mate = False
                                noMateMoves.append([i, j, i+ii, j+jj])
                            testBoard = deepcopy(board)
    else:
        mate = False

    return mate, noMateMoves

def simpleRating(board):
    rating = 0
    kings = []
    whiteQueens = []
    blackQueens = []
    for i, line in enumerate(board):
        for j, field in enumerate(line):
            if "Q" in field:
                if whitePlayerColor in field:
                    whiteQueens.append([i,j])
                else:
                    blackQueens.append([i, j])
            elif "K" in field:
                kings.append([i, j])
                """if whitePlayerColor in field:
                    whiteKing = [i, j]
                else:
                    blackKing = [i, j]"""
    for king in kings:
        for queen in whiteQueens:
            rating += 10*math.exp(-math.dist(king, queen))
        for queen in blackQueens:
            rating -= 10*math.exp(-math.dist(king, queen))

    return rating

def bestQueenMove(board, player, depth = 1):
    bestMove = [-1, -1]
    bestRating = -500
    playerWhite = True
    if player == blackPlayerColor:
        bestRating = 500
        playerWhite = False
    for i, line in enumerate(board):
        for j, field in enumerate(line):
            if player in field:
                if "K" in field or "Q" in field:
                    testBoard = deepcopy(board)
                    quantumMove(testBoard, j, i)
                    rating = simpleRating(testBoard)
                    if (rating > bestRating) == playerWhite:
                        bestMove = [j, i]
                        bestRating = rating
    return  bestMove, bestRating


def input2XY(s):
    x = -1
    y = -1
    if len(s) >= 2:
        x = "abcdefgh".find(s[0])
        y = "12345678".find(s[1])
    return x, y

def XY2input(x, y):
    s = ""
    if x in range(8) and y in range(8):
        s = "abcdefgh"[x] + str(y + 1)
    return s


init()
b = newBoard()
quantumMove(b, *input2XY("e2"))
quantumMove(b, *input2XY("e7"))
quantumMove(b, *input2XY("d1"))
quantumMove(b, *input2XY("d8"))
showBoard(b)
lastBoard = deepcopy(b)
bestMove = "h4"
while True:
    s = input("In: ").lower()
    if not s:
        s = bestMove
    if s in "new":
        lastBoard = deepcopy(b)
        b = newBoard()
    elif s in "back":
        b = deepcopy(lastBoard)
    else:
        xFrom, yFrom = input2XY(s)
        xTo, yTo = input2XY(s[2:])
        if xFrom >= 0 and yFrom >= 0:
            player = whitePlayerColor
            if whitePlayerColor in b[yFrom][xFrom]:
                player = blackPlayerColor
            lastBoard = deepcopy(b)
            quantumMove(b, xFrom, yFrom, xTo, yTo, ("p" in s))
            print("Rating:", "{0:.1f}".format(simpleRating(b)))
            m, r = bestQueenMove(b, player)
            bestMove = XY2input(*m)
            print("Best rated move:", bestMove, "{0:.1f}".format(r))
            m, nmm = checkmate(b, player)
            if m:
                print("Mate!")
            elif nmm:
                print("Check!")
                print("Possible moves:", [XY2input(*move[:2]) for move in nmm])

    showBoard(b)
