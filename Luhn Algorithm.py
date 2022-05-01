def LuhnAlgorithm():
    listCardNumber = []
    listOfDoubles = []

    while True:
        cardNumber = input("Enter an account number: \n")

        if cardNumber.isnumeric() and len(cardNumber) == 16:
            for character in cardNumber:
                listCardNumber.append(character)
            break

        else:
            print("Incorrect input")

    checkDigit = listCardNumber.pop()
    cardNumber = cardNumber[0:-1]

    for i in range(0, len(cardNumber), 2):
        doubleNumber = int(cardNumber[i]) * 2
        doubleNumber = str(doubleNumber)
        if len(doubleNumber) > 1:
            doubleNumber = int(doubleNumber[0]) + int(doubleNumber[1])
        listOfDoubles.append(int(doubleNumber))

    sumOne = 0

    for i in range(1, len(cardNumber), 2):
        sumOne = sumOne + int(cardNumber[i])

    totalSum = sumOne + sum(listOfDoubles)

    totalSum = str(totalSum)
    digitToMinus = int(totalSum[-1])
    digitToCheck = 10 - digitToMinus

    if digitToCheck == int(checkDigit):
        return True

    else:
        return False


print(LuhnAlgorithm())
