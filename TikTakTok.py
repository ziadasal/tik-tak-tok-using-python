def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def get_move(board):
    while True:
        try:
            row = int(input("Enter the row number (0, 1, or 2): "))
            col = int(input("Enter the column number (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win(board, player):
    for row in board:
        if all(square == player for square in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    for row in board:
        for square in row:
            if square == "":
                return False
    return True

def tic_tac_toe():
    game_board = [["" for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_idx = 0

    while True:
        print_board(game_board)
        current_player = players[player_idx]
        print(f"Player {current_player}'s turn.")
        row, col = get_move(game_board)
        game_board[row][col] = current_player

        if check_win(game_board, current_player):
            print_board(game_board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(game_board):
            print_board(game_board)
            print("It's a tie!")
            break

        player_idx = (player_idx + 1) % 2

if __name__ == "__main__":
    tic_tac_toe()
