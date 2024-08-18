import sys

def main():
    if check_arg_length() == False and sys.argv < 2:
      sys.exit('Too few command-line arguments')
    elif check_arg_length() == False and sys.argv > 2:
       sys.exit('Too many command-line arguments')
    else:
       ...


def check_arg_length():
    return len(sys.argv) == 2

def check_end():
   return sys.argv[1].endswith('.py')