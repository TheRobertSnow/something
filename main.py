### Declaring script variables ###

RANGE_START, RANGE_STOP = 1, 11 # Declaring range constants
x, o = 'x', 'o'
characterPosition = int(input('Input a position between 1 and 10: '))

### Script Fucntions ###

def printLine(position):        # Fucntion that prints the character line
    position = position
    for character in range(RANGE_START, RANGE_STOP):
        if character == position:
            print(o, end='')
        else:
            print(x, end='')

def moveCharacterLeft(position):    # Function that moves character o to the left
    position = position
    if position == 1:               # Make sure character doesn't go further than 1 to the left
        printLine(position)
        return position
    else:
        position -= 1
        printLine(position)
        return position             # Return the changed position value

def moveCharacterRight(position):   # Function that moves character o to the right
    position = position
    if position == 10:              # Make sure character doesn't go further than 10 to the right
        printLine(position)
        return position
    else:
        position += 1
        printLine(position)
        return position             # Return the changed position value

def waitForInput(position):    # Function that waits for user input and preformes the associated action
    position = position
    running = True              # Controller for while loop
    while running:
        if running == True:
            user_input = input('\nInput your choice: ')
            if user_input == 'r':
                position = moveCharacterRight(position)
            elif user_input== 'l':
                position = moveCharacterLeft(position)
            else:
                printLine(position)
                running = False

def startScript(characterPosition):     # Function that prints instructions on how to play
    position = characterPosition
    printLine(position)         # Print the line with the character
    print('\nl - for moving left')
    print('r - for moving right')
    print('Any other letter for quitting', end='')
    waitForInput(position)      # Call waitForInput() function


# Call startProgram()
startScript()
