class Color:
    PURPLE = '\033[95m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GRAY = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

continueRun='y'
while continueRun == 'y':
    usePrePrep = input("For the first object would you like to use pre programmed item? (this means you wont have to enter dimensions) " + Color.GREEN + "(y)es" + Color.END + Color.RED + " (n)o " + Color.END)
    if usePrePrep == 'y':
        print("(S)hopping cart")
        print("(B)ackpack")
        print("(E)mpire State building")
        whichPrePrep = input("Which previosly prepared objects would you like to use? ")
        if whichPrePrep == 'S':
            volumeObject = 27702
        if whichPrePrep == 'B':
            volumeObject = 605
        if whichPrePrep == 'E':
            volumeObject = 99110000
    else:
        lenght = int(input(Color.BLUE + "lenght" + Color.END + " of object 1: "))
        width = int(input(Color.RED + "width" + Color.END + " of object 1: "))
        height = int(input(Color.GREEN + "height" + Color.END + " of object 1: "))
        volumeObject=lenght*width*height
    
    usePrePrep = input("For the second object would you like to use pre programmed item (this means you wont have to enter dimensions) " + Color.GREEN + "(y)es" + Color.END + Color.RED + " (n)o " + Color.END)
    if usePrePrep == 'y':
        print("(S)hopping cart")
        print("(B)ackpack")
        print("(E)mpire State building")
        whichPrePrep = input("Which previosly prepared objects would you like to use? ")
        if whichPrePrep == 'S':
            surfaceObject = 5733
        if whichPrePrep == 'B':
            surfaceObject = 8970
        if whichPrePrep == 'E':
            surfaceObject = 1686076
    else:
        lenght1 = int(input(Color.BLUE + "lenght" + Color.END + " of object 2: "))
        width1 = int(input(Color.RED + "width" + Color.END + " of object 2: "))
        height1 = int(input(Color.GREEN + "height" + Color.END + " of object 2: "))
        surfaceObject=(2*lenght1*width1)+(2*lenght1*height1)+(2*height1*width1)
        
    print("The amount of the second object that can fit into the first object is " + str(volumeObject/surfaceObject))
    runAgain = input("\nwould you like to run the script again?\n" + Color.GREEN + "(Y)es" + Color.END + Color.RED + " (N)o " + Color.END)
    if runAgain == 'n':
        break