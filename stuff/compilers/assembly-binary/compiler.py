# compiles programs

import sys
import os





def compiler(source, binary, assemblyDict, fileName, binaryName):
    
    try:
        logs = open(f"./compiled-code/latest-log.log", "w")
    except:
        print("logging failed")

    for line in source:

        # logging and finding commands and args

        if line[0] != "#":
            command = line[0:3]
            


            arg2Confirm = False
            first = line.index("[")
            last = line.index("]")
            args = line[first:last+1]

            try:
                firstSpace = args.index(" ")
                arg1 = args[1:firstSpace]
                arg2Confirm = True
            except:
                arg1 = args[1:-1]
            
            

            if arg2Confirm == True:
                try:
                    n = 2
                    start = args.find(" ")
                    while start >= 0 and n > 1:
                        start = args.find(" ", start+len(" "))
                        n -= 1
                    
                    arg2 = args[start + 1:-1]
                    print(arg2)


                except:
                    print("an error has ocurred")









            logs.write(command + " [\n")
            logs.write("    " + arg1 + "\n")
            if arg2Confirm:
                logs.write("    " + arg2 + "\n")
            else:
                logs.write("    (no-arg)\n")
            logs.write("]\n")









        # compiling to binary

        binCommand = assemblyDict[command]

        if len(arg1) == 8:
            arg1Bin = arg1
        elif len(arg1) == 2:
            arg1Bin = assemblyDict[arg1[0]] + assemblyDict[arg1[1]]
        else:
            arg1Bin = assemblyDict[arg1]

        if arg2Confirm == True:
            if len(arg2) == 8:
                arg2Bin = arg2
            elif len(arg2) == 2:
                arg2Bin = assemblyDict[arg2[0]] + assemblyDict[arg2[1]]
            else:
                arg2Bin = assemblyDict[arg2]

        if arg2Confirm == False:
            binary.write(binCommand + "\n " + arg1Bin + "\n " + arg2Bin + "\n")
        else:
            binary.write(binCommand + "\n " + arg1Bin + "\n " + "00000000" + "\n")

        


    print(f"finished compiling {fileName} into binary file: {binaryName}")
    logs.close()
    binary.close()
    source.close()












fileName = input("please enter file name of program to compile\n>>> ")
logConfirmation = input("do you want a log file for the project? (yes / no)\n>>> ")
print(f"./source-code/{fileName}", "r")

try:
    source = open(f"./source-code/{fileName}", "r")
except:
    print("cant find file, check that you have the right directory")
    sys.exit()





binaryName = input("please enter filename for the binary file\n>>> ")
try:
    binary = open(f"./compiled-code/{binaryName}", "w")
except:
    print("cant find file, check that you have the right directory")
    sys.exit()    



assemblyDict = {

    # commands
    "MVE" : "00000001",
    "ADD" : "00000010",
    "SUB" : "00000011",
    "SFT" : "00000100",
    "JMP" : "00000101",
    "CND" : "00000110",
    "CLR" : "00000111",
    "END" : "00001000",
    "INP" : "00001001",
    "OUP" : "00001010",
    "LDA" : "00001011",
    "STA" : "00001100",
    "RMV" : "00001101",
    "VAR" : "00001110",

    # general purpose registers
    "REG-0" : "00000000",
    "REG-1" : "00000001",
    "REG-2" : "00000010",
    "REG-3" : "00000011",
    "REG-4" : "00000100",
    "REG-5" : "00000101",
    "REG-6" : "00000110",
    "REG-7" : "00000111",
    "REG-8" : "00001000",
    "REG-9" : "00001001",
    "REG-A" : "00001010",
    "REG-B" : "00001011",
    "REG-C" : "00001100",
    "REG-D" : "00001101",
    "REG-E" : "00001110",
    "REG-F" : "00001111",

    # special registers
    "ACC" : "00010000",
    "CPR" : "00010001",
    "MAR" : "00010010",
    "MDR" : "00010011",

    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "a" : "1010",
    "b" : "1011",
    "c" : "1100",
    "d" : "1101",
    "e" : "1110",
    "f" : "1111",

}


compiler(source, binary, assemblyDict, fileName, binaryName)





