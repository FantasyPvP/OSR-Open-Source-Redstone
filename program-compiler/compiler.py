# compiles programs

import sys



def compiler():
    for line in source:
        













fileName = sys.argv[0]
try:
    source = open(fileName, "r")
except:
    print("cant find file, check that you have the right directory")
    sys.exit()

binary = input("please enter filename for the binary file\n>>> ")
binary = open(f"./compiled-code/{binary}.txt", "w")


assemblyDict = {
    "MVE" : "00000000"
}












compiler(source, binary, dictionary)





