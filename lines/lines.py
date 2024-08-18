import sys

def main():
   ...


def check_arg_length():
    if len(sys.argv) < 2:
      sys.exit('Too few command-line arguments')
    elif len(sys.argv > 2):
       sys.exit('Too many command-line arguments')
    else:
       return True


def check_end():
   return True if sys.argv[1].endswith('.py') else sys.exit('Not a python file')