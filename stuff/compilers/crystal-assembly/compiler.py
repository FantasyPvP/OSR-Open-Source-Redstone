



class Tokeniser():
    def __init__(self):
        self.indentations = []
        self.charlists = []
        self.tokenlists = []
        self.currentChar = 0
        self.currentLine = 0


    def advance(self, chars):
        self.currentChar += chars


    def charLister(self, crystal):

        # filters through all lines in the program one by one to get a list of the characters on each line
        for line in crystal.readlines():
            if line != "\n":
                lineChars = []
                for char in line:
                    lineChars.append(char)
                    self.currentChar += 1

                # checks the indentation to see how many layers the line is indented
                for i in range(len(lineChars)):
                    if lineChars[i] != " ":
                        i -= 1
                        for x in range(i):
                            lineChars[i] = lineChars[i] + lineChars[x]


                        del(lineChars[0:i])
                        self.indentations.append(i)
                        break

                # adds list of characters to an array in the init function
                lineChars.pop(-1)
                self.charlists.append(lineChars)
            self.currentLine +=1
        del(self.charlists[0])
        crystal.close()




    def tokeniser(self):
        self.currentChar = 0
        self.currentLine = 0

        for x in range(len(self.charlists)):
            self.currentChar = 0
            tokenlist = []
            line = self.charlists[x]

            if line[0][0] == " ":
                tokenlist.append("LVL-" + str(len(line[0]) // 4))

            # makes tokens from each line
            endl = False
            while endl == False:
                char = line[self.currentChar]
                
                # inbuilt function ($), user function (@), return statement (&)

                if char == "$" or char == "@" or char == "&":
                    commandStart = line[self.currentChar:-1]
                    commandStart.append(line[-1])
                    commandEnd = commandStart[commandStart.index("(")]
                
                    command = commandStart[0:commandStart.index("(")]
                    command = "".join(command)
                    tokenlist.append(command)
                    tokenlist.append("(")

                    if commandStart.index(")") == commandStart.index("(") + 1:
                        tokenlist.append(")")

                


                    commandLen = len(command)
                    if self.currentChar == len(line) -1:
                        endl = True
                    else:
                        self.advance(commandLen -1)

                if self.currentChar == len(line) -1:
                    endl = True 
                else:   
                    self.advance(1)



            self.currentLine += 1
            self.tokenlists.append(tokenlist)




        return
        











def compiler(crystal, assembly, logs):
    tokeniser = Tokeniser()
    logger = Logger()
    tokeniser.charLister(crystal)
    tokeniser.tokeniser()
    logger.log(tokeniser)
    



class Logger():
    def __init__(self):
        return

    def log(self, tokeniser):

        logfile = open("./compiled-code/latest-log.log", "w")
        # logging charlists for source code

        logfile.write("\n\nsource code:\n\n")
        for x in tokeniser.charlists:
            for y in x:
                logfile.write(y)
            logfile.write("\n")

        # logging all commands / keywords in the script

        logfile.write("\n\nlist of tokens found in program:\n\n")
        for x in tokeniser.tokenlists:
            for y in x:
                logfile.write(y + " ")
            logfile.write("\n")

        logfile.close()


















class AbstractSyntaxTree():
    def generator():
        return

class Compiler():
    def main():
        return

























crystal = open(f"./source-code/source.Cy", "r")
compiler(crystal, "sheesh", "sheeesh")














































"""

fileName = input("please enter file name of program to compile\n>>> ")
logConfirmation = input("do you want a log file for the project? (yes / no)\n>>> ")

try:
    crystal = open(f"./source-code/{fileName}.Cy", "r")
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

"""