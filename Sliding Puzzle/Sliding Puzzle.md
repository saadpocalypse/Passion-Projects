# Sliding Puzzle

<br>

## What it is
* A simple 3x3 sliding puzzle game.
* You slide a tile into its adjacent empty space.
* You repeat until puzzle is fully solved.

<br>

## How the game works
* The game was made using HTML, CSS and Javascript.
* I randomly pick one of the folders and asssign the images as sources to the `<img>` divs I make.
* The third image in every folder is blank, it is the empty tile that can be switched around.
* Each tile has a coordinate.
* When a tile is clicked, the program checks if an adjacent tile has the third image as its source.
* If it does, the sources for the two `<img>` divs are switched.

<br>

## How the shuffler works
* Randomly shuffling the tiles around does not ensure that the puzzle will be solvable. 
* Imagine an N-1 puzzle after it has been shuffled, where N is the total number of tiles. If we write the number of tiles starting from top right and ending on the bottom left (ignoring the blank tile), we can deduce whether or not the puzzle is solvable by checking the number of inversions. An inversion refers to every time a tile preceeds another tile with a lower number. If the total number of inversions is an odd number, it means that the puzzle is not solvable.
* Instead of randomly shuffling the tiles around, my program makes 200 random yet valid moves. 200 is an arbitrary number.

<br>

## How the solver works
* I could have solved the puzzle using any of the solving algorithms. I did this initially but the puzzles got solved almost instantly since N is 9.
* Instead I created a function that logs the counter move of every single move made in an array (including moves made during shuffling) and when the user hits the solve button, the array is parsed and each element of the array is passed as an argument to a function that moves the tiles around.
* This solves the puzzle by moving backwards from the move at which the solve button is clicked. It takes longer and in my opinion, looks cooler.
