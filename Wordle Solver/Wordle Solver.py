def incorrectWordsExcluder(arrayWords, arrayCopy, letter):
    for wordChosen in arrayWords:
        if letter not in wordChosen:
            arrayCopy.append(wordChosen)

    arrayWords.clear()
    arrayWords = arrayCopy.copy()
    arrayCopy.clear()
    return arrayWords, arrayCopy


def partiallyIncorrectWordsExcluder(arrayWords, arrayCopy, letter, position):
    for wordChosen in arrayWords:
        if wordChosen[position - 1] != letter and letter in wordChosen:
            arrayCopy.append(wordChosen)

    arrayWords.clear()
    arrayWords = arrayCopy.copy()
    arrayCopy.clear()
    return arrayWords, arrayCopy


def correctWordsIsolator(arrayWords, arrayCopy, letter, position):
    for wordChosen in arrayWords:
        if wordChosen[position - 1] == letter:
            arrayCopy.append(wordChosen)

    arrayWords.clear()
    arrayWords = arrayCopy.copy()
    arrayCopy.clear()
    return arrayWords, arrayCopy


def main():
    listOfWords = []
    with open('Wordle Words.txt') as file:
        for line in file:
            for word in line.split():
                listOfWords.append(word.upper())
    inputToUse = 0
    conditionOne = False
    wordsLeft = []
    while True:
        print("\nYou have {0} possible word(s) left.\n".format(len(listOfWords)))
        while not conditionOne:
            inputOne = input("\nWhat do you want to do?\n1) Enter incorrect Letters\n2) Enter correct letters"
                             "\n3) Enter partially correct letters\n4) See the options I have\n"
                             "5) End program\n")

            try:
                inputOne = int(inputOne)
                if 0 < inputOne <= 5:
                    conditionOne = True
                    inputToUse = inputOne
                else:
                    print("Incorrect input, try again!")

            except:
                print("Incorrect input, try again!")

        conditionOne = False

        if inputToUse == 1:
            while True:
                inputTwo = input("Enter the letters that are incorrect (e.g ALKE): \n")
                inputTwo = inputTwo.upper()
                inputTwo = inputTwo.strip()
                if len(inputTwo) >= 1 and inputTwo.isalpha():
                    for char in inputTwo:
                        listOfWords, wordsLeft = incorrectWordsExcluder(listOfWords, wordsLeft, char)
                    break
                else:
                    print("Incorrect input!")

        if inputToUse == 4:
            print(*listOfWords, sep = ", ", end = ".")

        if inputToUse == 3:
            while True:
                inputChar = input("Enter the partially correct letter: \n")
                if inputChar.isalpha() and len(inputChar) == 1:
                    inputChar = inputChar.upper()
                    break
                else:
                    print("Incorrect input!")
            while True:
                inputNum = input("Enter the position that it is at (1 - 5): \n")
                try:
                    inputNum = int(inputNum)
                    if 1 <= inputNum <= 5:
                        break
                except:
                    print("Incorrect input!")
            listOfWords, wordsLeft = partiallyIncorrectWordsExcluder(listOfWords, wordsLeft, inputChar, inputNum)

        if inputToUse == 2:
            while True:
                inputChar = input("Enter the correct letter: \n")
                if inputChar.isalpha() and len(inputChar) == 1:
                    inputChar = inputChar.upper()
                    break
                else:
                    print("Incorrect input!")
            while True:
                inputNum = input("Enter the position that it is at (1 - 5): \n")
                try:
                    inputNum = int(inputNum)
                    if 1 <= inputNum <= 5:
                        break
                except:
                    print("Incorrect input!")
            listOfWords, wordsLeft = correctWordsIsolator(listOfWords, wordsLeft, inputChar, inputNum)

        if inputToUse == 5:
            print("Thanks for playing!\n-----PROGRAM TERMINATED-----")
            break


main()
