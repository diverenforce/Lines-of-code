import sys

def main():
    if arg_length() == False and len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif arg_length() == False and len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')

    if arg_end() != True:
       sys.exit('Not a python file')
    
    if arg_exist():
        sys.exit('File does not exist')

    counter = 0
    with open(sys.argv[1]) as File:
        for line in File:
            if line.isspace() or line[0] == '#':
                continue
            else:
                counter += 1
    
    print(counter)

def arg_length():
    return len(sys.argv) == 2

def arg_end():
   return sys.argv[1].endswith('.py')

def arg_exist():
    return sys.argv[1] == None