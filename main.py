userInput = -2 # unused initialized value

# Main game loop
while(userInput != -1):

    print("\n Enter -1 to exit")
    print("\n Enter 0 for new game\n\n")

    # Initialize variables
    cardList = []

    lowerCount = 0
    higherCount = 0
    equalCount = 0
    totalCount = 0

    userInput = -2 # unused initialized value


    # Initialize deck
    for suit in range(4):
        for card in range(2,15):
            cardList.append(card)

    cardList.sort()

    # Loop for each round
    while(userInput != 0 or userInput != -1):

        userInput = input("Enter value dealt : ")
        userInput = int(userInput)

        if userInput in cardList:
            cardList.remove(userInput)

        for card in cardList:
            totalCount += 1

            if(card < userInput):
                lowerCount += 1
            
            elif(card == userInput):
                equalCount += 1

            elif(card > userInput):
                higherCount += 1
        
        percentLower = (lowerCount / totalCount) * 100
        percentHigher = (higherCount / totalCount) * 100
        print("Lower%: " + str(round(percentLower, 0)) + "    " + "Higher%: " + str(round(percentHigher, 0)) + "\n")5

    