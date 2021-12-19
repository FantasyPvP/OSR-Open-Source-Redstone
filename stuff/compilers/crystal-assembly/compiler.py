def main(assembly, logs):
    global tokeniser
    global logger 

    tokeniser = Tokeniser()
    logger = Logger()

    tokeniser.charLister(crystal)
    tokeniser.tokeniser()

    logger.source(tokeniser.charlists)
    logger.tokens(tokeniser.tokenlists)
    










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
        if self.currentChar == len(line) - 1:
            endl = True
            return(endl)
        else:
            self.currentChar += (tokenLen - 1)
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
                tokenlist.append("LVL-" + str(len(line[0]) // 4) + " " * len(line[0]))
            else:
                tokenlist.append("LVL-0")

            # makes tokens from each line
            endl = False
            while endl == False:
                char = line[self.currentChar]

                # string handling
                if char == ":":
                    tokenlist.append(char)
                    endl = self.advance(line, 1)

                if char == '"':
                    tokenStart = line[self.currentChar:-1]
                    tokenStart.append(tokenStart[-1])
                    tokenStartA = tokenStart[1:]
                    tokenStartA.append(tokenStart[-1])
                    tokenEnd = tokenStartA[tokenStartA.index('"')]
                    token = tokenStart[0:tokenStartA.index('"') + 2]
                    token = "".join(token)
                    tokenlist.append(f"STR-{token}")
                    tokenLen = len(token)
                    endl = self.advance(line, tokenLen)

                # ints

                elif char.isnumeric():
                    string = ""
                    for i in line[self.currentChar:]:
                        string += i
                        if not(string[-1].isnumeric()):
                            token = string[0:-1]
                            tokenlist.append(f"INT-{token}")
                            endl = self.advance(line, len(token))
                            break

                # inbuilt function ($), user function (@), return statement (&)

                elif char == "$" or char == "@" or char == "&":
                    print("works")
                    tokenStart = line[self.currentChar:-1]
                    tokenStart.append(line[-1])
                    tokenEnd = tokenStart[tokenStart.index("(")]
                    
                    token = tokenStart[0:tokenStart.index("(")]
                    token = "".join(token)
                    tokenlist.append(token)
                    print(token, "token")
                    tokenLen = len(token)
                    endl = self.advance(line, tokenLen)


                elif char == "~":
                    string = "~"
                    for i in line[self.currentChar+1:]:
                        string += i
                        if not(string[-1].isalpha() or string[-1].isnumeric() or string[-1] == "_"):
                            token = string[1:-1]
                            tokenlist.append(f"CLASS-{token}")
                            endl = self.advance(line, len(token)+1)
                            break
                        

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
                    tokenlist.append(token)

                # declarators

                elif "".join(line[self.currentChar:self.currentChar + 3]) == "INT":
                    tokenlist.append("TYPE-INT")
                    endl = self.advance(line, 3)
        
                elif "".join(line[self.currentChar:self.currentChar + 3]) == "STR":
                    tokenlist.append("TYPE-STR")
                    endl = self.advance(line, 3)

                elif "".join(line[self.currentChar:self.currentChar + 4]) == "BOOL":
                    tokenlist.append("TYPE-BOOL")
                    endl = self.advance(line, 4)

                elif "".join(line[self.currentChar:self.currentChar + 4]) == "CHAR":
                    tokenlist.append("TYPE-CHAR")
                    endl = self.advance(line, 4)


                # inbuilt methods

                elif "".join(line[self.currentChar:self.currentChar + 4]) == "loop":
                    tokenlist.append("INBUILT-LOOP")
                    endl = self.advance(line, 4)
                elif "".join(line[self.currentChar:self.currentChar + 2]) == "if":
                    tokenlist.append("INBUILT-IF")
                    endl = self.advance(line, 2)
                elif "".join(line[self.currentChar:self.currentChar + 4]) == "elif":
                    tokenlist.append("INBUILT-ELIF")
                    endl = self.advance(line, 4)
                elif "".join(line[self.currentChar:self.currentChar + 4]) == "else":
                    tokenlist.append("INBUILT-ELSE")
                    endl = self.advance(line, 4)
                elif "".join(line[self.currentChar:self.currentChar + 4]) == "pass":
                    tokenlist.append("INBUILT-PASS")
                    endl = self.advance(line, 4)
                elif "".join(line[self.currentChar:self.currentChar + 5]) == "break":
                    tokenlist.append("INBUILT-BREAK")
                    endl = self.advance(line, 5)
                elif "".join(line[self.currentChar:self.currentChar + 5]) == "while":
                    tokenlist.append("INBUILT-WHILE")
                    endl = self.advance(line, 5)
                elif "".join(line[self.currentChar:self.currentChar + 5]) == "class":
                    tokenlist.append("INBUILT-CLASS")
                    endl = self.advance(line, 5)
                elif "".join(line[self.currentChar:self.currentChar + 8]) == "function":
                    tokenlist.append("INBUILT-FUNCTION")
                    endl = self.advance(line, 8)


                # variables

                elif char.isalpha():
                    string = ""
                    for i in line[self.currentChar:]:
                        string += i
                        if not(string[-1].isalpha() or string[-1].isnumeric() or string[-1] == "_"):
                            token = string[0:-1]
                            tokenlist.append(f"VAR-{token}")
                            endl = self.advance(line, len(token))
                            break
                
                
                print(char)
                endl = self.advance(line, 2)


            self.currentLine += 1
            self.tokenlists.append(tokenlist)

        return
        


class compiler():
    compiler












































class AbstractSyntaxTree():
    def generator():
        return

class Compiler():
    def main():
        return





















class Logger():
    def __init__(self):
        logfile = open("./compiled-code/latest-log.log", "w")
        logfile.write("logs for compilation of file: ./source-code/source.Cy")


    def source(self, source):
        logfile = open("./compiled-code/latest-log.log", "a")

        # logging charlists for source code

        logfile.write("\n\nsource code:\n\n")
        for x in source:
            print(x, "source")
            for y in x:
                print(y, "char")
                logfile.write(y)
            logfile.write("\n")

        logfile.close()


    def tokens(self, tokens):
        logfile = open("./compiled-code/latest-log.log", "a")
    
        # logging all commands / keywords in the script

        logfile.write("\n\nlist of tokens found in program:\n\n")
        for x in tokens:
            for y in x:
                logfile.write(y)
                logfile.write(" ")
            logfile.write("\n")

        logfile.close()

    def compilingErrors():
        return
    



global crystal
crystal = open(f"./source-code/source.Cy", "r")
main("sheesh", "sheeesh")






































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