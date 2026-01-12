#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # éviter la ligne après la dernière
            print("-" * 5)

def check_winner(board):
    # Vérifier les lignes
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    # Vérifier les colonnes
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Vérifier les diagonales
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def board_full(board):
    # Vérifier si toutes les cases sont remplies
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Saisie sécurisée
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position. Row and column must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Changer de joueur
        player = "O" if player == "X" else "X"

# Lancer le jeu
tic_tac_toe()
