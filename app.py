import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))
brokenWikiFileURL = currentDirectory + '/brokenWiki.txt'
fixedString = None
with open(brokenWikiFileURL, 'r+') as f:
    brokenText = f.read()
    print("BROKEN %s" % brokenText)

    foundAmpIndex = brokenText.find('&amp;')

    while foundAmpIndex != -1:

        # &amp;amp;amp;amp;amp;quot;
        startIndex = foundAmpIndex
        currentIndex = startIndex

        firstTime = True
        removableValues = ['&amp;', 'amp;']

        valueToCheck = brokenText[(currentIndex):(currentIndex + 5)]

        while valueToCheck in removableValues:
            print('Value To Check : %s' % valueToCheck)
            if firstTime:
                currentIndex += 5
                firstTime = False
            else:
                currentIndex += 4

            valueToCheck = brokenText[(currentIndex):(currentIndex + 4)]

        print(brokenText[(currentIndex):(currentIndex + 4)])

        brokenText = brokenText[:startIndex] + "'" + brokenText[currentIndex + 5]
        print('Removed string from index %d to %d' % (startIndex, (currentIndex + 5)))

        foundAmpIndex = brokenText.find('&amp;')

        # print(brokenText[(currentIndex):(foundAmpIndex + 5)])
        foundAmpIndex = -1

    # fixedString = brokenText.replace(";amp", "'")

    # print("FIXED %s" % fixedString)
    f.write(brokenText)
