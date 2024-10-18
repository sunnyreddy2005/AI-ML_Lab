import chess
import chess
import webbrowser

def print_board(board):
    print(board)

def get_player_move():
    move = input("Enter your move (in UCI format, e.g., e2e4): ")
    return move

def play_game():
    board = chess.Board()
    print_board(board)

    # Initialize the engine
    engine_path = "path/to/your/stockfish/executable"
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        while not board.is_game_over():
            if board.turn == chess.WHITE:
                # Player's move
                move = get_player_move()
                if chess.Move.from_uci(move) in board.legal_moves:
                    board.push(chess.Move.from_uci(move))
                else:
                    print("Illegal move. Try again.")
                    continue
            else:
                # AI's move
                result = engine.play(board, chess.engine.Limit(time=2.0))
                board.push(result.move)

            print_board(board)

        print("Game over!")
        print("Result: ", board.result())

    # After the game ends, open a new website
    new_website_url = "https://www.example.com"
    webbrowser.open(new_website_url)

if __name__ == "__main__":
    play_game()
