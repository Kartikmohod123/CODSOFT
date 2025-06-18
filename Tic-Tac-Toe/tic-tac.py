board = [" " for _ in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    print("Your turn, player")
    while True:
        try:
            choice = int(input("Enter your move (1-9): ").strip())
            if choice < 1 or choice > 9:
                print("Invalid input! Please enter a number between 1 and 9.")
            elif board[choice - 1] == " ":
                board[choice - 1] = icon
                break
            else:
                print("That space is already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def is_victory(icon):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(board[a] == board[b] == board[c] == icon for a, b, c in win_combos)

def is_draw():
    return " " not in board

def minimax(board_state, is_maximizing):
    if is_victory("O"):
        return 1
    elif is_victory("X"):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "O"
                score = minimax(board_state, False)
                board_state[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "X"
                score = minimax(board_state, True)
                board_state[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float("inf")
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
    print("AI chose position {}".format(move + 1))

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    while True:
        print_board()
        player_move("X")
        if is_victory("X"):
            print_board()
            print("You win! 🎉")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break

        print_board()
        ai_move()
        if is_victory("O"):
            print_board()
            print("AI wins! 🤖")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
