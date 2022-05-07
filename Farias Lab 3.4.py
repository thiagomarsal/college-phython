# IT 280 – Lab #5: Dictionary Validation Lab Instructions
import csv

# chessBoard = {
#     'a1': 'r', 'b1': 'n', 'c1': 'b', 'd1': 'q', 'e1': 'k', 'f1': 'b', 'g1': 'n', 'h1': 'r',
#     'a2': 'p', 'b2': 'p', 'c2': 'p', 'd2': 'p', 'e2': 'p', 'f2': 'p', 'g2': 'p', 'h2': 'p',
#     'a3': '.', 'b3': '.', 'c3': '.', 'd3': '.', 'e3': '.', 'f3': '.', 'g3': '.', 'h3': '.',
#     'a4': '.', 'b4': '.', 'c4': '.', 'd4': '.', 'e4': '.', 'f4': '.', 'g4': '.', 'h4': '.',
#     'a5': '.', 'b5': '.', 'c5': '.', 'd5': '.', 'e5': '.', 'f5': '.', 'g5': '.', 'h5': '.',
#     'a6': '.', 'b6': '.', 'c6': '.', 'd6': '.', 'e6': '.', 'f6': '.', 'g6': '.', 'h6': '.',
#     'a7': 'P', 'b7': 'P', 'c7': 'P', 'd7': 'P', 'e7': 'P', 'f7': 'P', 'g7': 'P', 'h7': 'P',
#     'a8': 'R', 'b8': 'N', 'c8': 'B', 'd8': 'Q', 'e8': 'K', 'f8': 'B', 'g8': 'N', 'h8': 'R',
# }

chessBoard = {
    'a': ['r', 'p', '.', '.', '.', '.', 'P', 'R'],
    'b': ['n', 'p', '.', '.', '.', '.', 'P', 'N'],
    'c': ['b', 'p', '.', '.', '.', '.', 'P', 'B'],
    'd': ['q', 'p', '.', '.', '.', '.', 'P', 'Q'],
    'e': ['k', 'p', '.', '.', '.', '.', 'P', 'K'],
    'f': ['b', 'p', '.', '.', '.', '.', 'P', 'B'],
    'g': ['n', 'p', '.', '.', '.', '.', 'P', 'N'],
    'h': ['r', 'p', '.', '.', '.', '.', 'P', 'R'],
}


def acceptRules():
    print('[Warning]: lowercase represents whites and uppercase represents blacks.')
    while True:
        answer = input("Answer '[y/Y]' to agree and continue or [n/N] to exit. ")
        if 'y' == answer.lower():
            return True
        elif 'n' == answer.lower():
            print('Good Bye!!!')
            return False
        else:
            print('Please, answer the question agreeing with the rules accordingly to move forward.')


def readFile(fileName):
    fileName = '/chess_board.csv'
    try:
        file = open(fileName, "r")
    except:
        print('An error occur while opening a file:', fileName)
    return file


def filterBy(key, values):
    filtered = filter(lambda s: key.lower() == s.lower(), values)
    return list(filtered)


def validateFile(fileName):
    try:
        column = []
        rows = []
        pieces = []

        with open(fileName, 'r') as file:
            reader = csv.reader(file)
            column = next(reader)
            for row in reader:
                rows.append(row)
                for item in row:
                    if item:
                        pieces.append(item)
            file.close()

        pawns = filterBy('p', pieces)
        rocks = filterBy('r', pieces)
        knights = filterBy('n', pieces)
        bishops = filterBy('b', pieces)
        queens = filterBy('q', pieces)
        kings = filterBy('k', pieces)

        isColumnValid = len(column) == 8
        isRowValid = len(rows) <= 8
        isPiecesValid = len(pieces) <= 32
        isPawnValid = len(pawns) <= 16
        isKnightValid = len(knights) <= 4
        isRockValid = len(rocks) <= 4
        isBishopValid = len(bishops) <= 4
        isQueenValid = len(queens) <= 2
        isKingValid = len(kings) <= 2

        print('[{0}]\t Columns validation. Value: {1}'.format(isColumnValid, len(column)))
        print('[{0}]\t Rows validation. Value: {1}'.format(isRowValid, len(rows)))
        print('[{0}]\t Contains a maximum of 32 pieces. Value: {1}'.format(isPiecesValid, len(pieces)))
        print('[{0}]\t Contains a maximum of 16 pawns. Value: {1}'.format(isPawnValid, len(pawns)))
        print('[{0}]\t Contains a maximum of 4 knights. Value: {1}'.format(isKnightValid, len(knights)))
        print('[{0}]\t Contains a maximum of 4 rocks. Value: {1}'.format(isRockValid, len(rocks)))
        print('[{0}]\t Contains a maximum of 4 bishops. Value: {1}'.format(isBishopValid, len(bishops)))
        print('[{0}]\t Contains a maximum of 2 queen. Value: {1}'.format(isQueenValid, len(queens)))
        print('[{0}]\t Contains a maximum of 2 king. Value: {1}'.format(isKingValid, len(kings)))
        print()
    except:
        print('[Error]: An error occurred while opening a file:', fileName)
    if isColumnValid and isRowValid and isPiecesValid and isPawnValid and isKingValid and isRowValid and isBishopValid and isQueenValid and isKingValid:
        return rows


def printChessBoard(chessBoard):
    print("|---------------------------|")
    print("|       Chess Board         |")
    print("|---------------------------|")
    print()
    print("\t____________________")
    for column in chessBoard.keys():
        print("\t" + column, end="| ")
        for row in chessBoard.get(column):
            if row and row.strip():
                print(row, end=" ")
            else:
                print('.', end=" ")
        print(" | ")
    print("\t____________________")
    print()


def createChessBoard(items):
    board = dict.fromkeys(chessBoard.keys(), [])
    for key, value in enumerate(board):
        board[value] = items[key]
    return board

def main():
    if acceptRules():
        printChessBoard(chessBoard)

        files = ["./chess_board.csv", "./chess_board_invalid.csv"]
        for file in files:
            print('Starting validation for file=', file)
            items = validateFile(file)
            if items:
                board = createChessBoard(items)
                printChessBoard(board)
            else:
                print('Sorry, your file contain an issue. Please, make sure you have the correct values.')


main()
