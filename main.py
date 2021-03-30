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

        # Grab user input for this hand
        userInput = input("Enter value dealt : ")
        userInput = int(userInput)

        # Reset values so they can be recounted
        lowerCount = 0
        higherCount = 0
        equalCount = 0
        totalCount = 0

        # Check input and remove dealt card from the list
        if userInput in cardList:
            cardList.remove(userInput)

        else:
            print("Invalid Input\n\n\n\n")
            break

        # Track values for later calculations
        for card in cardList:
            totalCount += 1

            if(card < userInput):
                lowerCount += 1
            
            elif(card == userInput):
                equalCount += 1

            elif(card > userInput):
                higherCount += 1
        
        # Calculate final percentages
        percentLower = (lowerCount / totalCount) * 100
        percentHigher = (higherCount / totalCount) * 100
        percentEqual = (equalCount / totalCount) * 100

        # Print data for user to view
        print("Lower%: " + str(round(percentLower, 0)) + "      " + "Higher%: " + str(round(percentHigher, 0))+ "       " + "Equal%: " + str(round(percentEqual, 0)) + "\n")
        print("#Lower: " + str(lowerCount) + "      " + "#Higher: " + str(higherCount) + "      " + "#Equal: " + str(equalCount) + "\n")
        print("Cards Left: " + str(totalCount) + "\n")

    