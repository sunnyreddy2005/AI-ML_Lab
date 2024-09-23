# Represent the Tic-Tac-Toe board as a list of 9 elements
# 'X' is the maximizing player, 'O' is the minimizing player, and '' is an empty space

def print_board(board):
    """Helper function to print the Tic-Tac-Toe board."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board):
    """Check if there is a winner."""
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                        (0, 4, 8), (2, 4, 6)]
    
    for (a, b, c) in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != '':
            return board[a]
    
    if '' not in board:
        return 'Draw'
    
    return None

def minmax(board, depth, is_maximizing):
    """Min-Max algorithm implementation."""
    winner = check_winner(board)
    
    if winner == 'X':
        return 10 - depth
    if winner == 'O':
        return depth - 10
    if winner == 'Draw':
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                eval = minmax(board, depth + 1, False)
                board[i] = ''
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                eval = minmax(board, depth + 1, True)
                board[i] = ''
                min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    """Find the best move for the maximizing player 'X'."""
    best_val = float('-inf')
    move = -1
    for i in range(9):
        if board[i] == '':
            board[i] = 'X'
            move_val = minmax(board, 0, False)
            board[i] = ''
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Example usage:
if __name__ == "__main__":

    board = ['X', 'O', 'X',
             'O', 'X', '',
             '',  '', 'O']
    
    print("Current Board:")
    print_board(board)
    
    move = best_move(board)
    print(f"The best move for 'X' is at position {move}")
    board[move] = 'X'

    print("Board after 'X' move:")
    print_board(board)