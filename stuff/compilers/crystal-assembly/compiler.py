



class tokeniser():
    def tokenise(self, crystal, assembly):
        return









class AbstractSyntaxTree():
    def generator():
        return

class Compiler():
    def main():
        return



def compiler(crystal, assembly, logs):
    tokeniser.tokenise(crystal)

















































fileName = input("please enter file name of program to compile\n>>> ")
logConfirmation = input("do you want a log file for the project? (yes / no)\n>>> ")

try:
    source = open(f"./source-code/{fileName}.Cy", "r")
except:
    print("cant find file, check that you have the right directory")
    sys.exit()





assemblyName = input("please enter filename for the crystal file\n>>> ")
try:
    assembly = open(f"./compiled-code/{assemblyName}.Cy-A", "w")
except:
    print("cant find file, check that you have the right directory")
    sys.exit()
compiler(crystal, assembly, logs)