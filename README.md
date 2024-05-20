## Battleships-Prela

Ultimate Battleships-Prela is a Python terminal game, which runs on Heroku.
Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. 
Each battleship occupa one square on the board.

* Live link: 
[Here is the live version of my project.](https://battleship-prela-805a22d0542f.herokuapp.com/)


![Screen responsiveness](/media/responsive.png)


## How to play

Ultimate Battleships is based on the classic pen-and-paper game. You can read more about it on [Wikipedia.](https://en.wikipedia.org/wiki/Battleship_(game)).
In this version, the player enters their name and two boards are randomly generated.
The player can see where their ships are, indicated by an @ sign, but cannot see where the computer's ships are.
Guesses are marked on the board with an X. Hits are indicated by *
The player and the computer then take it in turns to make guesses and try to sink each other's battleships.
The winner is the player who sinks all of their opponent's battleships first.

## User Stories

###  User Story 1: Player Registration
 - As a player, I want to enter my name at the start of the game, so that I can personalize my gaming experience.

### User Story 2: Player's Board Visibility
 - As a player, I want to see the locations of my own battleships indicated by the @ sign on my board, so that I know where my ships are placed.

### User Story 3: Hidden Computer's Board
 - As a player, I want to be unable to see the locations of the computer’s battleships, so that the game maintains a level of challenge and surprise.

### User Story 4: Guessing Mechanism
 - As a player, I want to be able to make guesses about the locations of the computer’s battleships, so that I can try to sink them by marking hits and misses.

### User Story 5: Hit and Miss Indicators
 - As a player, I want to see an X on the board where a guess is made and a * where a hit is made, so that I can track my progress and strategy.

### User Story 6: Winning Condition
 - As a player, I want to win the game by sinking all of the computer's battleships, so that I can achieve victory.

### User Story 7: Computer's Turn Logic
 - As a player, I want the computer to make intelligent guesses to try and find my battleships, so that the game is challenging and engaging.

### User Story 8: Game Instructions
 - As a new player, I want to read clear instructions on how to play the game, so that I can understand the rules and mechanics before starting.

### User Story 9: Game Feedback
 - As a player, I want to receive feedback after each guess (hit, miss, or invalid guess), so that I know the result of my actions immediately.

### User Story 10: Game Restart
 - As a player, I want to have the option to restart the game after it ends, so that I can play again without having to reload the program.

These user stories should give a comprehensive overview of the player's experience and expectations when playing Ultimate Battleships-Prela.

## Flowchart

![Flowchart](/media/flowchart.png)

## Features
### Existing Features

  -  Random board generation.
  -  Ships are randomly placed on both the player and computer boards.
  -  The player cannot see where the computer's ships are.

![Welcome](/media/welcome_game_msg.png)

  -  Play against the computer.
  -  Accepts user input.
  -  Maintains scores.

![Enter-Start](/media/enter_name_start_game.png)

  -  Input validation and error-checking
  -  You cannot enter coordinates outside the size of the grid.
  -  You must enter numbers.
  -  You cannot enter the same guess twice.
 
![Error](/media/error-invalid-coordinates.png)

![Enter](/media/enter_row_enter_column.png)

  -  Data maintained in class instances

## Future Features

  -  Allow player to select the board size and number of ships.
  -  Allow player to position ships themselves.
  -  Have ships larger than 1x1.

## Data Model

I decided to use a Board class as my model. The game creates two instances of the Board class to hold the player's and the computer's
board.
The Board class stores the board size, the number of ships, the position of the ships, the guesses against that board, and details such as the board type 
(player's board or computer) and the player's name.
The class also has methods to help play the game, such as a print method to print out the current board, an add_ships method to add ships to the board and 
an add_guess method to add a guess and return the result.

## Technology Used
  -  Python 
  -  GitHub 
  -  Gitpod
  -  Heroku

## Testing

I have manually tested this project by doing the following:

Passed the code through a PEP8 linter and confirmed there are no problems.

  -  Given invalid inputs: strings when numbers are expected and out of bounds inputs.
  -  Tested in my local terminal and Heroku terminal.

### Test Case 1: Invalid Row and Column Input
 - Test Name: Test Invalid Row Input
 - Description: Verify that the game correctly handles an invalid row input by the player.
 - Steps: Start the game and enter a valid player name. At the prompt to enter a guess, input a coordinate with an invalid row or column.

 ![Enter](/media/test_cases_1_invalid_row_invalid_column.png)

### Test Case 2: Valid Row and Column Input
 - Test Name: Test Valid Row and Column Input
 - Description: Verify that the game correctly processes a valid row and column input by the player.
 - Steps: Start the game and enter a valid player name. At the prompt to enter a guess, input a coordinate with a valid row and column

 ![Enter](/media/test_cases_2_valid_row_valid_column.png)

## Bugs

### Solved Bugs

  -  My validate_coordinates function was returning false positives because I hadn't structured the if statement properly.

### Remaining Bugs

  -  No bugs remaining.

### Validator Testing

  -  PEP8.

  -  No errors were returned from[PEP8](https://pep8ci.herokuapp.com/#)

![Error check](/media/ci_python_linter_error_check.png)

## Deployment

This project was deployed using Heroku.

-  Steps for deployment:

   -  Fork or clone this repository.
   -  Create a new Heroku app.
   -  Set the buildbacks to Python and NodeJS in that order.
   -  Link the Heroku app to the repository.
   -  Click on Deploy.

## Forking the repository
In order to fork the repository to make a copy the steps are:

1. Log into GitHub and locate the repository for https://github.com/ROCK3879/Battleship.git
2. At the top of the repository above settings locate the 'Fork' button There is now a copy of the repository in the Github account.

-----
Happy coding!
