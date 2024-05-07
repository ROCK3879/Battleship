## Battleships-Prela

Ultimate Battleships-Prela is a Python terminal game, which runs on Heroku.
Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. 
Each battleship occupa one square on the board.

* Live link: 
[Here is the live version of my project.](https://------------------------.heroku)


![Screen responsiveness](/media/responsive.png)


## How to play

Ultimate Battleships is based on the classic pen-and-paper game. You can read more about it on [Wikipedia.](https://en.wikipedia.org/wiki/Battleship_(game)).
In this version, the player enters their name and two boards are randomly generated.
The player can see where their ships are, indicated by an @ sign, but cannot see where the computer's ships are.
Guesses are marked on the board with an X. Hits are indicated by *
The player and the computer then take it in turns to make guesses and try to sink each other's battleships.
The winner is the player who sinks all of their opponent's battleships first.

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
