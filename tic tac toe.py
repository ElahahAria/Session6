print("hello this is tic-tak-toe game: ")

from pyfiglet import Figlet


def bazi():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()


def barresi():
    # v1
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("winner is player 1, X ")
        return True
    # v2
    elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print("winner is player 1, X")
        return True
    # v3
    elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print("winner is player 1, X")
        return True
    # h1
    elif game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print("winner is player 1, X")
        return True
    # h2
    elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("winner is player 1, X")
        return True
    # h3
    elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("winner is player 1, X")
        return True
    # m1
    elif game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("winner is player 1, X")
        return True
    # m2
    elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
        print("winner is player 1, X")
        return True
    return False


def barresi2():
    # v1
    if game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print("winner is player 2, O ")
        return True
    # v2
    elif game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        print("winner is player 2, O  ")
        return True
    # v3
    elif game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
        print("winner is player 2, O  ")
        return True
    # h1
    elif game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print("winner is player 2, O  ")
        return True
    # h2
    elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print("winner is player 2, O  ")
        return True
    # h 3
    elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("winner is player 2, O ")
        return True
    # m1
    elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("winner is player 2, O  ")
        return True
    # m2
    elif game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
        print("winner is player 2, O  ")
        return True
    return False


f = Figlet(font='slant')
print(f.renderText('Tic-Tac-Toe'))

game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]
bazi()

turns = 0

while True:
    # Player1
    print("Player 1: ")
    row = int(input("Ent row: "))
    col = int(input("Ent  col: "))
    if 0 <= row <= 2 and 0 <= col <= 2:
        if game_board[row][col] == "-":
            game_board[row][col] = "X"
            bazi()
            if barresi():
                break
            turns += 1
        else:
            print("tekrari! ")
    else:
        print("mahdude mojaz:(0-2)")

    # Check for tie
    if turns == 9:
        print("no winner! draw")
        break

    # Player2
    print("Player 2: ")
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    if 0 <= row <= 2 and 0 <= col <= 2:
        if game_board[row][col] == "-":
            game_board[row][col] = "O"
            bazi()
            if barresi2():
                break
            turns += 1
        else:
            print("tekrari!")
    else:
        print("mahdude mojaz:(0-2).")

    # Check for tie
    if turns == 9:
        print("draw, try again")
        break
