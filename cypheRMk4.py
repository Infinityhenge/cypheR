import os
def program():
    numKey1 = os.urandom(2)
    numKey2 = int(numKey1[0])
    numKey3 = int(numKey1[1])
    numKey = [numKey2, numKey3]
    inpoot = input("Code or Decode, c/d: ")
    if inpoot == "c":
        def encode():
            inp = input("Input your sentence to be encoded: ")
            ex = list(inp)
            length = len(inp)
            file = open("your code.txt", "w")

            for blue in range(0, length):
                red = ex[blue]
                coded = ord(red)
                calculation = coded+numKey[0]+numKey[1]
                calculation2 = str(calculation)
                file.write(calculation2 + " ")
            file.write("\nYour number keys for decoding are:"+str(numKey[0])+" "+str(numKey[1]))
            print("Your codes were written to a text file in the same directory as this program")
            print("")
            print("press 'enter' to return")
        encode()
        input()
        program()
    elif inpoot == "d":
        def decode():
            stringIn = input("Please input your code to decode: ")
            numKeyIn = input("Please input your two number keys separated by a space: ")
            numKeyArr = numKeyIn.split(" ")
            realLength1 = stringIn.split("-")
            realLength2 = len(realLength1) - 1
            lenth = realLength2
            seperatedToArray = stringIn.split("-")
            for gi in range(0, lenth):
                red = seperatedToArray[gi]
                toInt = int(red)
                calculation = toInt-int(numKeyArr[0])-int(numKeyArr[1])
                coded = chr(calculation)
                print(coded, end="")
        decode()
        print("")
        print("Press 'enter' to return")
        input()
        program()
    else:
        print("Wrong input")
        program()
program()
