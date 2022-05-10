def mainFour():
    dictionaryOfWords = {}
    import re
    import operator
    import matplotlib.pyplot as plotter

    with open('beeMovie.txt', 'r') as fileOne:

        for lineRead in fileOne:

            for wordRead in lineRead.split():
                wordRead = wordRead.lower()
                if not bool(re.search('^[a-zA-Z0-9]*$', wordRead)):
                    continue

                if wordRead in dictionaryOfWords:
                    dictionaryOfWords[wordRead] = dictionaryOfWords[wordRead] + 1

                else:
                    dictionaryOfWords[wordRead] = 1

    sortedDictionary = dict(sorted(dictionaryOfWords.items(), key=operator.itemgetter(1), reverse=True))
    xAxis = []
    yAxis = []
    counterDictionary = 0
    for key in sortedDictionary:
        if counterDictionary == 20:
            break
        xAxis.append(key)
        yAxis.append(sortedDictionary[key])
        counterDictionary = counterDictionary + 1

    plotter.plot(xAxis, yAxis)
    plotter.xlabel("Words")
    plotter.ylabel("Repetitions")
    plotter.title("Most common words in the script of the Bee Movie (2007)")
    plotter.show()


mainFour()
