import string


def main():
    inputOne = input("Enter the name of a disease: \n").lower()
    inputTwo = input("Enter the name of an organ: \n").lower()
    inputThree = input("Enter the name of a different disease: \n").lower()
    inputFour = input("Enter a relative (husband, uncle, son, etc): \n").lower()
    inputFive = input("Enter the name of a food: \n").lower()
    inputSix = input("Enter the name of a body part: \n").lower()
    inputSeven = input("Enter the name of a liquid: \n").lower()
    inputEight = input("Enter an emotion: \n").lower()
    inputNine = input("Enter an adjective: \n").lower()
    inputTen = input("Enter another emotion: \n").lower()
    inputEleven = input("Enter a verb (present tense without 'ing'): \n").lower()
    inputTwelve = input("Enter the name of a body part: \n").lower()
    inputThirteen = input("Enter the name of a disease: \n").lower()
    inputFourteen = input("Enter any number: \n")
    inputFifteen = input("Enter the name of anything you read: \n").lower()
    inputSixteen = input("Enter the name of any celebrity: \n")
    inputSixteen = string.capwords(inputSixteen)
    inputSeventeen = input("Enter the name of a food: \n").lower()
    inputEighteen = input("Enter the name of another celebrity: \n")
    inputEighteen = string.capwords(inputEighteen)
    inputNineteen = input("Enter the name of a place: \n")
    inputNineteen = string.capwords(inputNineteen)
    inputTwenty = input("Enter a name: \n")
    inputTwenty = string.capwords(inputTwenty)
    inputTwentyOne = input("Enter the name of another place: \n")
    inputTwentyOne = string.capwords(inputTwentyOne)
    inputTwentyTwo = input("Enter any number: \n")
    inputTwentyThree = input("Enter the name of any food: \n").lower()

    print("Oh you have \033[4m{0}\033[0m? So your \033[4m{1}\033[0m doesn't work, right? Well at least you \ndon't have"
          " \033[4m{2}\033[0m. My \033[4m{3}\033[0m has it and got it because they ate too much \033[4m{4}\033[0m.\n"
          "Last year, they had their \033[4m{5}\033[0m cut off! I hear you can cure it by drinking \033[4m{6}\033[0m?\n"
          "I feel \033[4m{7}\033[0m for you because those \033[4m{8}\033[0m needles would make me \033[4m{9}\033[0m.\n"
          "And I could never have someone \033[4m{10}\033[0m one of those pump things in my \033[4m{11}\033[0m. \n"
          "My cousin had \033[4m{12}\033[0m but outgrew it when she turned \033[4m{13}\033[0m. I was reading \n"
          "in \033[4m{14}\033[0m that \033[4m{15}\033[0m had it but reversed it by eating nothing \n"
          "but \033[4m{16}\033[0m, and \033[4m{17}\033[0m has it and they've lived a long life with no problems. I \n"
          "also read that a lot of people who have it bad travel to \033[4m{18}\033[0m because they have a cure for\n"
          "it there. Don't sweat it, Dr. \033[4m{19}\033[0m said that there will be a cure discovered \n"
          "in \033[4m{20}\033[0m in about \033[4m{21}\033[0m years. Then you can start eating \033[4m{22}\033[0m \n"
          "again!".format(inputOne, inputTwo, inputThree, inputFour, inputFive, inputSix, inputSeven, inputEight,
                          inputNine, inputTen, inputEleven, inputTwelve, inputThirteen, inputFourteen, inputFifteen,
                          inputSixteen, inputSeventeen, inputEighteen, inputNineteen, inputTwenty, inputTwentyOne,
                          inputTwentyTwo, inputTwentyThree))


main()
