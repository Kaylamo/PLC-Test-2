# change out files to count the lexemes and see if it has any syntax errors
file = open("willrun1.py")

# math symbols --
operators = {'=': 'Equal', '+': 'Addition', '-': 'Subtraction', '/': 'Division',
             '*': 'Multiplication', '<': 'Less than', '>': 'Greater than', '%': 'Modular', '<=': 'Less than/Equal',
             '>=': 'Greater Than/Equal'}
# prgm will label the symbol based on whatever I used
operators_key = operators.keys()

# python data types present in my test files
data_type = {'int': 'integer type', 'float': 'Floating point', 'char': 'Character type', 'long': 'long int',
             'str': 'string'}
# prgm will label data types in my code
data_type_key = data_type.keys()

# different punctuations present -- prgm will label which ones were used in my code
punctuation_symbol = {':': 'colon', ';': 'semi-colon', '.': 'dot', ',': 'comma'}
punctuation_symbol_key = punctuation_symbol.keys()

# variables used -- only a--d
identifier = {'a': 'id', 'b': 'id', 'c': 'id', 'd': 'id'}
identifier_key = identifier.keys()
# condition is met
dataFlag = False
# will read whatever file is present above
a = file.read()
# count --- which line we are on
count = 0
# counts the line and parses through it to count the lexemes within it
program = a.split("\n")
for line in program:
    count = count + 1
    print("Line ", count, "\n", line)
    # tokens -- basically all the lexemes within a line
    tokens = line.split(' ')
    print("Tokens are ", tokens)
    print("Line ", count, "properties \n")
    # searches for the information above and names the lexeme
    for token in tokens:
        if token in operators_key:
            print("operator: ", operators[token])
        if token in data_type_key:
            print("datatype: ", data_type[token])
        if token in punctuation_symbol_key:
            print(token, "Punctuation: ", punctuation_symbol[token])
        if token in identifier_key:
            print(token, "Identifier: ", identifier[token])
    # program stops running
    dataFlag = False
    # separates each line of information
    print("++++++++++++++++++++++++++++++++++++++++++++++")


# Syntax Error Parser

def main():
    # read file
    # must put file into parser to find errors
    file = open("lexicalerror.py", "r")
    lines = file.readlines()
    file.close()
    # look for the syntax error
    countError = 0
    countNone = 0
    for line in lines:
        line = line.strip()
        # look for the error
        if line.find("error") != -1:
            countError = countError + 1
        if line.find("NO") != -1:
            countNone = countNone + 1

    # results
    print("Syntax Error count:  ", countError)


main()
