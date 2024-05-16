from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    # Main board class. Sets board size, the number of ships, the player's name and the board type (player board or computer) 
    # Has methods for adding ships and guesses and printing the board
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self): 
        for row in self.board: 
            print(" ".join(row))

    def guess(self, x, y): 
        self.guesses.append((x, y)) 
        if (x, y) in self.ships: 
            self.board[x][y] = "*" 
            return "Hit"
        else:
            self.board[x][y] = "x"
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y)) 
            if self.type == "player": 
                self.board[x][y] = "@"

def random_point(size):
    # Helper function to return a random integer between 0 and size
    return randint(0, size - 1)

def valid_coordinates(x, y, board):
    # Check if coordinates are within the board size
    return 0 <= x < board.size and 0 <= y < board.size

def populate_board(board):
    # Add ships randomly to the board
    while len(board.ships) < board.num_ships:
        x = random_point(board.size)
        y = random_point(board.size)
        if valid_coordinates(x, y, board) and (x, y) not in board.ships:
            board.add_ship(x, y)

def make_guess(board):
    # Take a guess from the user
    try:
        x = int(input("Enter row: "))
        y = int(input("Enter column: "))
        if not valid_coordinates(x, y, board):
            print("Invalid coordinates! Try again.")
            make_guess(board)
        else:
            result = board.guess(x, y)
            print("Result:", result)
    except ValueError:
        print("Invalid input! Try again.")
        make_guess(board)

def play_game(computer_board, player_board):
    """ Play the game """
    while True:
        print("Computer's Board:")
        computer_board.print()
        print("\nYour Board:")
        player_board.print()
        print("\n")
        
        print("Your Turn:")
        make_guess(computer_board)
        print("\n")
        
        print("Computer's Turn:")
        computer_guess_x = random_point(player_board.size)
        computer_guess_y = random_point(player_board.size)
        result = player_board.guess(computer_guess_x, computer_guess_y)
        print(f"Computer guessed ({computer_guess_x}, {computer_guess_y}) - Result: {result}")
        print("\n")

        if all((x, y) in player_board.guesses for x in range(player_board.size) for y in range(player_board.size)):
            print("Congratulations! You've won!")
            scores["player"] += 1
            break
        elif all((x, y) in computer_board.guesses for x in range(computer_board.size) for y in range(computer_board.size)):
            print("Computer wins!")
            scores["computer"] += 1
            break

def get_player_name() :
   while True:
     player_name = input("Please enter your name: \n").strip()
     if len(player_name) > 1 and len(player_name) < 15:
            return player_name
     else:
        print("Player name should be within 15 characters")  

def new_game():
    # Start a new game
    size = 5
    num_ships = 4

    scores["computer"] = 0
    scores["player"] = 0

    print("-" * 35)
    print(" Welcome to ULTIMATE BATTLESHIPS!!")
    print(f" Board Size: {size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35)

    player_name = get_player_name()

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)

if __name__ == '__main__':

    new_game()
