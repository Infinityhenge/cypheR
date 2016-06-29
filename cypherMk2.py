def program():
    inpoot = input("Code or Decode, c/d: ")
    if inpoot == "c":
        def encode():
            inp = input("Input your sentence to be encoded: ")
            ex = list(inp)
            length = len(inp)

            for blue in range(0, length):
                red = ex[blue]
                coded = ord(red)
                calculation = ((coded+7)+500)
                print(calculation, end="-")
            print("")
            print("press 'enter' to return")
        encode()
        input()
        program()
    elif inpoot == "d":
        def decode():
            stringIn = input("Please input your code to decode: ")
            realLength1 = stringIn.split("-")
            realLength2 = len(realLength1) - 1
            lenth = realLength2
            seperatedToArray = stringIn.split("-")
            for gi in range(0, lenth):
                red = seperatedToArray[gi]
                toInt = int(red)
                calculation = ((toInt-500)-7)
                coded = chr(calculation)
                print(coded, end="")
        decode()
        input()
        print("Press 'enter' to return")
        program()
    else:
        print("Wrong input")
        program()
program()
