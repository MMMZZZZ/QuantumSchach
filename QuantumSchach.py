from colorama import init, Fore, Back, Style
import math

fieldSizeX = 3
fieldSizeY = 1
fieldEmpty = " "
previewMarker = "."
# [Dark Field Color, Light Field Color]
previewBackColors = [Back.YELLOW, Back.LIGHTYELLOW_EX]
normalBackColors = [Back.BLACK, Back.WHITE]
whitePlayerColor = Fore.LIGHTWHITE_EX
blackPlayerColor = Fore.LIGHTBLACK_EX

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
                    printableField[fieldSizeX // 2] = field
                printableLine.append(printableField)
            printableBoard.append(printableLine)

    print("  ", " " * (fieldSizeX // 2), sep = "", end = "")
    for i in range(8):
        print(chr(ord("A") + i) + " " * (fieldSizeX - 1), end = "")
    print("")
    for i in range(len(printableBoard)):
        if (i + fieldSizeY // 2 + 1) % fieldSizeY == 0:
            print((len(printableBoard) - i - 1) // fieldSizeY + 1, " ", sep = "", end = "")
        else:
            print("  ", end = "")
        for field in printableBoard[len(printableBoard) - 1 - i]:
            print("".join(field), end = "")
        print(Style.RESET_ALL, end = "")
        if (i + fieldSizeY // 2 + 1) % fieldSizeY == 0:
            print(" ", (len(printableBoard) - i - 1) // fieldSizeY + 1, sep = "")
        else:
            print("  ")
    print("  ", " " * (fieldSizeX // 2), sep = "", end="")
    for i in range(8):
        print(chr(ord("A") + i) + " " * (fieldSizeX - 1), end = "")
    print("")
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

def quantumMove(board, x, y, preview):
    piece = board[y][x]
    newPositions = []
    pieceColor = ""
    if whitePlayerColor in piece:
        pieceColor = whitePlayerColor
    elif blackPlayerColor in piece:
        pieceColor = blackPlayerColor

    for i,line in enumerate(board):
        for j,field in enumerate(line):
            board[i][j] = field.replace(previewMarker, "")

    if "P" in piece:
        if pieceColor == whitePlayerColor:
            if y < 7:
                if board[y + 1][x] == fieldEmpty:
                    newPositions.append([y + 1, x])
                if y == 1 and board[3][x] == fieldEmpty:
                    newPositions.append([3, x])
                if x > 0:
                    if blackPlayerColor in board[y + 1][x - 1]:
                        newPositions.append([y + 1, x - 1])
                if x < 7:
                    if blackPlayerColor in board[y + 1][x + 1]:
                        newPositions.append([y + 1, x + 1])
        elif pieceColor == blackPlayerColor:
            if y > 0:
                if board[y - 1][x] == fieldEmpty:
                    newPositions.append([y - 1, x])
                if y == 6 and board[4][x] == fieldEmpty:
                    newPositions.append([4, x])
                if x > 0:
                    if whitePlayerColor in board[y - 1][x - 1]:
                        newPositions.append([y - 1, x - 1])
                if x < 7:
                    if whitePlayerColor in board[y - 1][x + 1]:
                        newPositions.append([y - 1, x + 1])
    elif "N" in piece or "K" in piece:
        moves = ""
        if "N" in piece:
            moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        elif "K" in piece:
            moves = [[0, 1], [0, -1], [1, 1], [1, 0], [1, -1], [-1, 1], [-1, 0], [-1, -1]]
        for move in moves:
            nextX = x + move[0]
            nextY = y + move[1]
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
            nextX = x
            nextY = y
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

    if newPositions:
        for position in newPositions:
            if preview:
                board[position[0]][position[1]] += previewMarker
            else:
                board[position[0]][position[1]] = piece
        if not preview:
            board[y][x] = fieldEmpty

def input2XY(s):
    x = "abcdefgh".find(s[0])
    y = "12345678".find(s[1])
    return x, y

b = newBoard()
showBoard(b)
while True:
    s = input("In: ").lower()
    if s in "new":
        b = newBoard()
    else:
        nx, ny = input2XY(s)
        if nx >= 0 and ny >= 0:
            quantumMove(b, nx, ny, ("p" in s))
    showBoard(b)