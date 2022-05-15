# Wordle Solver

## How it works
I use a text file that contains all the words Wordle uses and thae file is filtered down with every guess made by the user. 

## How to use
### 1. Make a guess on Wordle.
<img width="371" alt="Screenshot 2022-05-15 at 5 05 42 AM" src="https://user-images.githubusercontent.com/64619851/168452026-95e54b74-932c-41be-a160-824ed7740a55.png">

***

### 2. As it is evident from the guess, the letters R, A, N and E are incorrect, so I put them in the program as incorrect letters.
<img width="399" alt="Screenshot 2022-05-15 at 5 06 08 AM" src="https://user-images.githubusercontent.com/64619851/168452040-793de207-aad4-4394-84c7-be4fa42fa8b1.png">

***

### 3. Since C is partially correct, I input it along with the position it is incorrectly placed at.
<img width="338" alt="Screenshot 2022-05-15 at 5 06 21 AM" src="https://user-images.githubusercontent.com/64619851/168452060-c66e0bdd-460b-486c-8f0e-2dd913725975.png">
We have now shortened the list of words from 12972 options down to 240, which is 1.85% of the original number of options.

***

### 4. Make the next guess on Wordle.
<img width="383" alt="Screenshot 2022-05-15 at 5 08 25 AM" src="https://user-images.githubusercontent.com/64619851/168452165-9cebaf08-d2e6-46d4-bba4-16d83f4ee930.png">

***

### 5. Now, the letters P and T are incorrect, so we feed them into the program as such.
<img width="391" alt="Screenshot 2022-05-15 at 5 06 59 AM" src="https://user-images.githubusercontent.com/64619851/168452200-decc8afa-e683-4388-bb4d-960d2bf4bd2f.png">

***

### 6. The letter S and O are at correct positions. We will put them into the program with their respective placements.
<img width="339" alt="Screenshot 2022-05-15 at 5 07 16 AM" src="https://user-images.githubusercontent.com/64619851/168452250-e7bb6b66-2025-437c-a91a-80134db3043b.png">
<img width="341" alt="Screenshot 2022-05-15 at 5 07 35 AM" src="https://user-images.githubusercontent.com/64619851/168452251-d1790fef-79e7-4e34-892d-7645805a89f9.png">

***

### 7. The letter U is partially correct. Like before, I will put it into the program along with its current position
<img width="338" alt="Screenshot 2022-05-15 at 5 07 48 AM" src="https://user-images.githubusercontent.com/64619851/168452276-7bd40249-6242-4980-84a6-2a5a814ea6fd.png">
In just two turns, we have narrowed the list from 12972 words to just 4, which is 0.03% of the original number of options.

***

### 8. Since we only have 4 words left, we can choose to view the options.
<img width="301" alt="Screenshot 2022-05-15 at 5 07 59 AM" src="https://user-images.githubusercontent.com/64619851/168452315-7f2acd4d-3062-480c-9116-b2a0a0d7bb4a.png">
At this point, we can afford to go one by one through the options left to see which one is correct.

***

### 9. Enter the options left in Wordle until you are correct.
<img width="355" alt="Screenshot 2022-05-15 at 5 15 12 AM" src="https://user-images.githubusercontent.com/64619851/168452333-48324485-325b-46a2-8530-51629a9539b7.png">

***

## Notes
* I have done all the error handling I could think of.
* If a letter is at a correct placement in the word and shows 'grey' at another placement in the same guess, do not input it as an incorrect letter. It is still part of the word, it may just mean it is not repeated twice in the word.
* The program can handle multiple repetitions of the same letter.
* Feel free to use and/or modify the program as you like.
