# Spelling Bee

## Rules
1. First, enter 6 surrounding letters.
2. After entering the surrounding letters, enter the central letter.
3. Once all the letters have been entered, you can begin making words made with the letters.
4. The words entered MUST include the central letter.
5. The words entered should be at least 4 letters long.
6. The words entered cannot have any letters except the ones in play.
7. The words entered cannot include special characters.

## Notes
* The game will end automatically when the user guesses all the possible words that can be made.
* The game can be called off at any moment, causing the program to terminate after displaying all the possible words.
* The user can view the words that have been guessed at any point in the game.
* I have tried my best to handle all the edge cases and errors.
* When reading the _.txt_ file containing all the words, I isolate the words that are longer than the length of 3 and have no more than 7 unique letters, since these are the only words that can be accepted. This is to make the program a bit more efficient.
* I make 26 different arrays, each one containing words starting from a specific letter. I only parse the appropriate array to validate the words that are entered.
* I made a function to check for pangrams as well. If the word entered by the user comprises of all the letters in play, the user is notified that the word entered was a pangram.
* When the game is ended, user stats are returned as well as all the pangrams that could've been made.
