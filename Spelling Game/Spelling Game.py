import random


def uniqueCounter(wordArg):
    unique = []
    for char in wordArg[::]:
        if char not in unique:
            unique.append(char)
    return len(unique)


listOfWords = []

with open('words.txt') as file:
    for line in file:
        for word in line.split():
            if len(word) > 3 and uniqueCounter(word) <= 7:
                listOfWords.append(word)
counter = 0
dictionary = [[], [], [], [], [], [], [], [], [], [], [], [], [],
              [], [], [], [], [], [], [], [], [], [], [], [], []]
alphabet = "abcdefghijklmnopqrstuvwxyz"
printerList = []

for word in listOfWords:
    dictionary[alphabet.index(word[0])].append(word)

listOfLetters = []


def makeBoard():
    lettersDone = []
    for i in range(0, 6):
        while True:
            inputOne = input("Enter a letter: \n")
            inputOne = inputOne.strip()
            num = intCheck(inputOne)
            if not num or len(inputOne) != 1 or inputOne in lettersDone:
                print("Incorrect input!")
            else:
                listOfLetters.append(inputOne.upper())
                printerList.append(inputOne.upper())
                lettersDone.append(inputOne)
                break

    while True:
        inputTwo = input("Enter the central letter: \n")
        inputTwo = inputTwo.strip()
        num = intCheck(inputTwo)
        if not num or len(inputTwo) != 1 or inputTwo in lettersDone:
            print("Incorrect input!")
        else:
            return inputTwo.upper()


def printBoard(letters, central):
    print("    {0}   {1}".format(letters[0], letters[1]))
    print("  {0}   {1}   {2}".format(letters[2], central, letters[3]))
    print("    {0}   {1}".format(letters[4], letters[5]))


def intCheck(arg):
    flag = True
    for char in arg:
        if char.isnumeric():
            flag = False

    return flag


def endGame(centerArg):
    listOfAll = []
    empty = []
    for element in listOfLetters:
        for wordCurrent in dictionary[alphabet.index(element.lower())]:
            result, printer = wordChecker(wordCurrent, empty, centerArg)
            if result:
                listOfAll.append(wordCurrent.upper())

    return listOfAll


def wordChecker(wordArg, listDone, center):
    wordArg = wordArg.strip()

    if wordArg == "!":
        return False, "End"

    elif wordArg == "":
        return False, "Shuffled!"

    elif wordArg == "?":
        print("You have guessed {0} words: ".format(len(listDone)))
        for element in listDone:
            print(element)

    else:
        wordArg = wordArg.upper()

        if len(wordArg) <= 3:
            return False, "Word is too short!"

        elif center not in wordArg:
            return False, "Missing the middle letter!"

        elif wordArg in listDone:
            return False, "Word done already!"

        else:
            wordArg = wordArg.lower()
            if wordArg not in dictionary[alphabet.index(wordArg[0])]:
                return False, "Word does not exist!"
            else:
                flagWord = True
                for char in wordArg:
                    if char.upper() not in listOfLetters:
                        flagWord = False
                if not flagWord:
                    return False, "Bad letters!"
                else:
                    listDone.append(wordArg.upper())
                    return True, "Accepted!"


def main():
    wordsDone = []
    centralLetter = makeBoard()
    listOfLetters.append(centralLetter)

    print(
        "\nKeep entering words, leave empty to reshuffle, "
        "enter '!' to end game and '?' to see words you have done."
        "\nTo end the game and see all the words that could have been formed, enter '!!'.")
    while True:
        print()
        printBoard(printerList, centralLetter)
        inputTwo = input("\n")
        if inputTwo.strip() == "?":
            print("You have guessed {0} word(s): ".format(len(wordsDone)))
            wordsDone.sort()
            for element in wordsDone:
                print(element)
        else:
            if inputTwo == "!!":
                finalList = endGame(centralLetter)
                print("All the words that could have been: ")
                finalList.sort()
                for wordArg in finalList:
                    print(wordArg)
                print("Thanks for playing!")
                print("-----PROGRAM TERMINATED-----")
                break
            result, printer = wordChecker(inputTwo, wordsDone, centralLetter)

            if not result:
                if printer == "Shuffled!":
                    random.shuffle(printerList)

                if printer == "End":
                    print("You guessed {0} word(s): ".format(len(wordsDone)))
                    for element in wordsDone:
                        print(element)
                    print("Thanks for playing!")
                    print("-----PROGRAM TERMINATED-----")
                    break

                else:
                    print(printer)

            else:
                print(printer)


main()
