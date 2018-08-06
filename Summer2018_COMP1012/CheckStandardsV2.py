"""
 COMP 1012  SECTION A01
 INSTRUCTOR Terry Andres
 ASSIGNMENT: Check Standards
 AUTHOR    Terry Andres
 VERSION   2016-Jan-12

 PURPOSE: check student code for adherence to standards and assign a mark
"""
#1234567891123456789212345678931234567894123456789512345678961234567897123456789
import builtins
import keyword
import re      # for regular expression analysis
import sys
from time import ctime
import tokenize
from tkinter import filedialog, Tk
#import traceback

DEBUG_LEVEL = 0 # controls which outputs to show
KEYWORDS = ( set(keyword.kwlist) | set(dir(builtins)) # | set(globals())
             | {"cmath", "end", "math", "m", "matplotlib", "np", "numpy", 
                "os", "plt", "pylab", "random","sys", "time"}) # not user words                         
MAX_ALLOWED = 2 # maximum number of violations allowed
MAX_AVG_NAME = 12 # max number of characters in the average name
MAX_LINE_LENGTH = 81 # max length of a line in characters, including \n
MIN_AVG_NAME = 4 # min number of characters in the average name

# Regular expression patterns
CONST_PATTERN = re.compile("^[A-Z0-9_]+$") # assumes a valid identifier
VAR_PATTERN = re.compile("^[a-zA-Z0-9]+$") # assumes a valid identifier
SHORT_PATTERN = re.compile("^[a-zA-Z0-9_]{2,3}$") # assumes a valid identifier

commentNeeded = False # whether there should be an end-of-line comment
numBadIndents = 0 # number of lines with nonstandard indents
numInvalidNames = 0 # number of invalid identifiers
numLongLines = 0 # number of lines with too many characters
numMissingComments = 0 # number of missing end of line comments
numMissingDocStrings = 0 # number of contexts without a doc string
warned = False # was there a warning on this line?

#..........................................................................main
def main() :
    """Code to read a file and assess its adherence to standards"""
    global fileDict
    
    fileDict = {}
    print("\nOpening a file—look for dialog box:")
    sys.stdout.flush()
    win = Tk() # root window for tkinter file dialog
    win.attributes('-topmost', True)
    win.withdraw() # hide root window
    win.lift() # move to front
    filename = filedialog.askopenfilename(parent=win) # get file name
    #            message="Pick a Python file to check") # label on dialog box
    win.destroy() # get rid of root window
    print("Opening file %s, assumed to be a Python file\n" % filename)
    analyzeFile(filename)

    if DEBUG_LEVEL > 0 :
        tokenParts = set(name for name in dir(tokenize) if name.isupper() 
                 and type(eval("tokenize." + name))==int) # tokenize constants
        tokenCodes = sorted([(eval("tokenize." + name),name) for 
                 name in tokenParts]) # codes corresponding to tokenParts
        print("\nTable of token codes")    
        for code, name in tokenCodes:
            print("%5d %s" % (code, name))
                                                         
    showTermination()
    return

#...................................................................analyzeFile
def analyzeFile(filename) :
    """
    Purpose: to return a set of canonical lines of code from filename.
    Parameters: filename is the name of a file containing Python code.
    Return:     None
    """
    global curLine, LINES, lineNum2
    global commentNeeded, numBadIndents, numInvalidNames, numLongLines
    global numMissingComments, numMissingDocStrings, warned

    nameDict = {} # dictionary of identifiers
    try :
        with open(filename, "r", encoding="utf-8") as fil : # 8-byte Unicode
            lines = fil.readlines() # all the lines of the file in a list
    except IOError as ex :
        print("#### Input error in %s" % filename)
        print("#### %s" % ex)
    lines[-1] += '\n' if lines[-1][-1] != '\n' else ''
    lines += ['']
    LINES = lines
    lineNum2 = -1
    curLine = ''
   
    try :
        tokens = tokenize.generate_tokens(getLine) # seq of tokens in file
        context = "program" # the scope being analyzed
        docStringNeeded = True # is a doc string needed next?
        prevToken = (0,'',(),(),0) # previous token to the current one
        count = 0 # count of tokens, to control how often to show debug lines
        for token in tokens :
            # Invariant: prevToken and token are two consecutive tokens
            #     in the code of filename
            # Invariant: count is the position of token in the sequence
            # Invariant: line is the current statement that includes token.
            #     It might occupy several lines. The line currently being 
            #     parsed is lineNum
            # Invariant: indent is the location of the first non-blank char 
            #     of the current statement.
            # Invariant: docStringNeeded says whether the current statement 
            #     should be a doc string
            count += 1
            if DEBUG_LEVEL > 0 and count % 10 == 0 :
                print("token: %d, %s" % token[:2])
            if token[0] == tokenize.COMMENT :
                commentNeeded = False
            if token[0] == tokenize.STRING :
                if docStringNeeded :
                    docStringNeeded = False
            elif token[0] == tokenize.NAME :
                if docStringNeeded :
                    print("     ** Missing doc string for %s" % context)
                    docStringNeeded = False
                    numMissingDocStrings += 1
                if prevToken[1] == "def" : # new function
                    context = "def function %s" % token[1]
                    
                invalid = checkName(token[1], lineNum2, prevToken[1], 
                                    nameDict) # 0 if valid, >0 if not
                warned = warned or invalid
                numInvalidNames += invalid
            elif token[0] in (tokenize.INDENT, tokenize.DEDENT) :
                indent = calcIndent(lines[lineNum2]) # num of chars indented
                    # print("    indent = %d" % indent)
                if indent == 0 :
                    context = "program"
                elif indent % 4 != 0 :
                    print("     ** Nonstandard indentation %d spaces" % indent)
                    warned = True
                    numBadIndents += 1
                else :
                    pass
            elif token[0] == tokenize.NEWLINE :
                if commentNeeded :                
                    print("     ** Missing end-of-line comment for new "
                          "variable '%s'" % commentNeeded)
                    warned = True
                    numMissingComments += 1
                commentNeeded = False
                if context.startswith("def ") :
                    context = context[4:]
                    docStringNeeded = True
                if DEBUG_LEVEL > 0 or warned :
                    print(curLine)
                    warned = False
                curLine = ''
            elif (token[0] == tokenize.OP 
                             and token.exact_type == tokenize.EQUAL) :
                if prevToken[0] == tokenize.NAME : # simple assignment
#                    print("1st locus of %s was %d; current %d"
#                          % (prevToken[1], nameDict[prevToken[1]][1], lineNum))
                    if (prevToken[1] in nameDict 
                       and nameDict[prevToken[1]][1] == lineNum2) :
                        commentNeeded = prevToken[1]
                        #print("New assignment of %s" % prevToken[1])
                    
            prevToken = token
        fil.close()
    except Exception as ex1 :
        print("#### Error detected in Python file %s" % filename)
        print("#### %s" % ex1)
#        print("#### %s" % traceback.print_last())
    #print globals()
    print("\nDeductions:")
    deduct = checkAllNames(nameDict) # mark deduction for problems detected
    if numLongLines > MAX_ALLOWED :
        print("-1: Too many (%d) excessively long lines" % numLongLines)
        deduct -= 1
    if numBadIndents > MAX_ALLOWED :
        print("-1: Too many (%d) badly indented sections" % numBadIndents)
        deduct -= 1
    if numInvalidNames > MAX_ALLOWED :
        print("-1: Too many (%d) nonstandard names" % numInvalidNames)
        deduct -= 1
    if numMissingComments > MAX_ALLOWED :
        print("-1: Too many (%d) missing end=of-line comments" 
            % numMissingComments)
        deduct -= 1
    if numMissingDocStrings > MAX_ALLOWED :
        print("-1: Too many (%d) missing doc strings" 
            % numMissingDocStrings)
        deduct -= 1        
    print ("Total deductions: %d" % deduct)
    return

#................................................................... calcIndent
def calcIndent(line) :
    """Return the number of spaces by which the line is indented."""
    indent = 0 # initial indent
    ch = '\n' # a character in line
    for ch in line :
        if ch == ' ' :
            indent += 1
        elif ch == '\t' :
            indent = (indent + 4) // 4 * 4
        else :
            break
    if ch == '\n' :
        indent = 0
    return indent


#.................................................................... checkName
def checkName(name, lineNum, prevTokenName, nameDict) :
    """Check that the name is valid, and record is usage. Updates nameDict
    but doesn't return anything."""
    count = 0
    if name in KEYWORDS or prevTokenName == '.' : 
        return 0
    if len(name) <= 1 :
        nameType = "invalid"  # invalid, short, constant, variable, or function
        count = 1
    elif SHORT_PATTERN.fullmatch(name) :
        nameType = "short"
    elif CONST_PATTERN.fullmatch(name) :
        nameType = "constant"
    elif VAR_PATTERN.fullmatch(name) :
        nameType = "variable"
    else :
        nameType = "invalid"
        count = 1
    if name in nameDict :
        nameDict[name].append(lineNum)
        count = 0 # don't count it again
    else :
        nameDict[name] = [nameType, lineNum]
        if nameType == "invalid" :
            print("     ** Nonstandard name: %s" % name)
    if prevTokenName == "def" :
        nameDict[name][0] = "function"
    return count
        
#................................................................ checkAllNames
def checkAllNames(nameDict) :
    """Check the average name length."""
    names = nameDict.keys() # unique identifiers found
    nameLens = [len(name) for name in names] # lengths in same order
    avgLength = sum(nameLens) / (len(nameLens)+0.001) # avg of var lengths
    deduct = 0 # number of points to deduct
    if avgLength < MIN_AVG_NAME :
        print("-1: Avg name length %.2g is too small; code will be unclear"
              % avgLength)
        deduct -= 1
    elif avgLength > MAX_AVG_NAME :
        print(("-1: Avg name length %.2g is too big; "
               "expressions will be hard to read")
              % avgLength)
        deduct -= 1
    return deduct
    

#...................................................................... getLine
def getLine() :
    """Retrieve the next line from lines--generator function"""
    global curLine, LINES, lineNum2, numLongLines, warned
    if lineNum2 < len(LINES) - 2 :
        lineNum2 += 1 # new line
        if len(LINES[lineNum2][:-1].rstrip() + '\n') > MAX_LINE_LENGTH :
            print("     ** Excessively long line (%d chars)"
                  % len(LINES[lineNum2]))
            numLongLines += 1
            warned = True
        curLine += ("%3d |%s" % (lineNum2+1, LINES[lineNum2]))
        return LINES[lineNum2]
    else :
        return ''
              
    
#...............................................................showTermination
def showTermination() :
    """
    Purpose: to print a final message identifying the programmer,
    giving the date, and saying the program has finished.
    """
    print ( "\nProgrammed by Terry Andres" )
    print(( "Date: " + ctime() ))
    print ( "End of processing" )

#................................................................default script

main()
