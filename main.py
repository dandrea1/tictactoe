from art import logo


def create_board():
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)


def display_board():
    print(board[0])
    print(board[1])
    print(board[2])


def game_finished():
    if ((board[0][0] != '-' and board[0][0] == board[0][1] == board[0][2])
            or (board[1][0] != '-' and board[1][0] == board[1][1] == board[1][2])
            or (board[2][0] != '-' and board[2][0] == board[2][1] == board[2][2])
            or (board[0][0] != '-' and board[0][0] == board[1][0] == board[2][0])
            or (board[0][1] != '-' and board[0][1] == board[1][1] == board[2][1])
            or (board[0][2] != '-' and board[0][2] == board[1][2] == board[2][2])
            or (board[0][0] != '-' and board[0][0] == board[1][1] == board[2][2])
            or (board[0][2] != '-' and board[0][2] == board[1][1] == board[2][0])):
        return True
    else:
        return False


def tie(count):
    # Since only 9 spaces on board, once count it 10 game is over.
    if count == 10:
        return True
    else:
        return False


def play_tic_tac_toe():
    game_on = True
    turn_count = 1  # first play of the game will always be X's
    print(logo)

    create_board()
    display_board()

    while game_on:
        # Check if there is a winner
        if game_finished():
            print(f"Winner winner chicken dinner.")
            game_on = False
        # Check if game ends in a draw
        elif tie(count=turn_count):
            print("Game ends in a draw.")
            game_on = False
        # Continue Game Play
        else:
            if turn_count % 2 != 0:
                turn = 'X'
            else:
                turn = 'O'
            move = input(f"Specify which row and column you want to place a {turn}. Ex. 2,3: ")
            row = int(move[0]) - 1
            column = int(move[2]) - 1
            # Check that user didn't use a position already used.
            if board[row][column] != '-':
                while board[row][column] != '-':
                    move = input(f"Sorry this position has already been used. \n"
                                 f"Specify which row and column you want to place a {turn}. Ex. 2,3: ")
                    row = int(move[0]) - 1
                    column = int(move[2]) - 1
            # Complete player's play.
            board[row][column] = turn
            turn_count += 1
        display_board()


wants_to_play = True
while wants_to_play:
    continue_playing = input("Do you want to play a game of tic tac toe? Y/N: ")
    if continue_playing == 'Y':
        # Reset Board
        board = []
        play_tic_tac_toe()
    else:
        wants_to_play = False
        print("thanks for playing.")
