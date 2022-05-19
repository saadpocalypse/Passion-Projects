# Spelling Bee

## Rules
1. First, enter 6 surrounding letters.
2. After entering the surrounding letters, enter the central letter.
<img width="239" alt="Screenshot 2022-05-20 at 2 04 15 AM" src="https://user-images.githubusercontent.com/64619851/169404582-04a7ff77-8b58-413e-9f19-664f79159f4d.png">
3. Once all the letters have been entered, you can begin making words made with the letters.

<img width="690" alt="Screenshot 2022-05-20 at 2 04 25 AM" src="https://user-images.githubusercontent.com/64619851/169404694-4447ccf1-1024-42df-9187-580afaccfd41.png">
5. The words entered MUST include the central letter.

<img width="143" alt="Screenshot 2022-05-20 at 2 04 44 AM" src="https://user-images.githubusercontent.com/64619851/169404760-fc9f3727-cec3-4253-acbb-2097a1ff1ec8.png">



7. The words entered should be at least 4 letters long.
8. The words entered cannot have any letters except the ones in play.
9. The words entered cannot include special characters.
10. Only words in the _.txt_ file are accepted as valid words.

## Notes
* The game will end automatically when the user guesses all the possible words that can be made.
* The game can be called off at any moment, causing the program to terminate after displaying all the possible words.

<img width="331" alt="Screenshot 2022-05-20 at 2 05 08 AM" src="https://user-images.githubusercontent.com/64619851/169404816-06b42b4b-0c64-43a8-92df-997ce431720a.png">


* The user can view the words that have been guessed at any point in the game.
<img width="234" alt="Screenshot 2022-05-20 at 2 04 54 AM" src="https://user-images.githubusercontent.com/64619851/169404875-1d83decf-00c3-47bd-b691-691328b9b7ce.png">


* I have tried my best to handle all the edge cases and errors.
* When reading the _.txt_ file containing all the words, I isolate the words that are longer than the length of 3 and have no more than 7 unique letters, since these are the only words that can be accepted. This is to make the program a bit more efficient.
* I make 26 different arrays, each one containing words starting from a specific letter. I only parse the appropriate array to validate the words that are entered.
* I made a function to check for pangrams as well. If the word entered by the user comprises of all the letters in play, the user is notified that the word entered was a pangram.
* When the game ends, user stats are returned as well as all the pangrams that could've been made.
<img width="331" alt="Screenshot 2022-05-20 at 2 05 08 AM" src="https://user-images.githubusercontent.com/64619851/169404959-48379936-3c23-49e5-8eb5-852130e359cb.png">



