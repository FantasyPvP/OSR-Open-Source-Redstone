



class Tokeniser():
    def __init__(self):
        self.indentations = []
        self.charlists = []
        self.tokenlists = []
        self.currentChar = 0
        self.currentLine = 0
        self.brackets = ["(", ")", "{", "}", "[", "]"]
        self.operators = ["=", ">", "<", "+", "-", "*", "/", "!"]
        self.inbuilts = ["INT", "STR", "BOOL"]


    def advance(self, line, tokenLen):
        if self.currentChar == len(line) -1:
            endl = True
            return(endl)
        else:
            self.currentChar += tokenLen
            endl = False
            return(endl)



    def charLister(self, crystal):

        # filters through all lines in the program one by one to get a list of the characters on each line
        for line in crystal.readlines():
            if line != "\n":
                lineChars = []
                for char in line:
                    lineChars.append(char)
                    self.currentChar += 1

                # checks the indentation to see how many layers the line is indented
                if lineChars[0] == " ":
                    for i in range(len(lineChars)):
                        if lineChars[i] != " ":
                            print(i, "i")
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
                    tokenStart = line[self.currentChar:-1]
                    tokenStart.append(line[-1])
                    tokenEnd = tokenStart[tokenStart.index("(")]
                
                    token = tokenStart[0:tokenStart.index("(")]
                    token = "".join(token)

                    tokenlist.append(token)
                    tokenlist.append("(")

                    if tokenStart.index(")") == tokenStart.index("(") + 1:
                        tokenlist.append(")")

                    tokenLen = len(token)
                    endl = self.advance(line, tokenLen)

                # string handling

                elif char == '"':
                    tokenStart = line[self.currentChar:-1]
                    tokenStart.append(tokenStart[-1])
                    tokenStartA = tokenStart[1:]
                    tokenStartA.append(tokenStart[-1])
                    tokenEnd = tokenStartA[tokenStartA.index('"')]
                    token = tokenStart[0:tokenStartA.index('"') + 2]
                    token = "".join(token)
                    tokenlist.append(token)

                    tokenLen = len(token)
                    endl = self.advance(line, tokenLen)

                # brackets / parenthesis

                elif char in self.brackets:
                    token = char
                    tokenlist.append(token)

                # operators

                elif char in self.operators:
                    try:
                        if line[self.currentChar + 1] in self.operators:
                            token = line[self.currentChar] + line[self.currentChar + 1]
                            tokenLen = 2
                        else:
                            token = char
                            tokenLen = 1
                    except:
                        token = char
                        tokenLen = 1

                    endl = self.advance(line, tokenLen)
                    print(token)
                    tokenlist.append(token)




                # declarators

                elif "".join(line[self.currentChar:self.currentChar + 3]) == "INT":
                    tokenlist.append("INT")
                    endl = self.advance(line, 3)
        
                elif "".join(line[self.currentChar:self.currentChar + 3]) == "STR":
                    tokenlist.append("STR")
                    endl = self.advance(line, 3)

                elif "".join(line[self.currentChar:self.currentChar + 4]) == "BOOL":
                    tokenlist.append("BOOL")
                    endl = self.advance(line, 4)

                elif "".join(line[self.currentChar:self.currentChar + 4]) == "CHAR":
                    tokenlist.append("CHAR")
                    endl = self.advance(line, 4)


                # inbuilt methods







                endl = self.advance(line, 1)


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
                logfile.write(y)
                logfile.write(" ")
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