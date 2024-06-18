def display_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def is_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell in ['X', 'O'] for cell in row) for row in board)

def make_move(board, player):
    valid_move = False
    while not valid_move:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and board[row][col] not in ['X', 'O']:
                board[row][col] = player
                valid_move = True
            else:
                print("Invalid move, try again.")
        else:
            print("Invalid input, try again.")

def main():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    current_player = 'X'
    game_won = False

    while not game_won and not is_board_full(board):
        display_board(board)
        make_move(board, current_player)
        game_won = is_winner(board, current_player)

        if game_won:
            display_board(board)
            print(f"Player {current_player} wins!")
        elif is_board_full(board):
            display_board(board)
            print("The game is a draw!")

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
