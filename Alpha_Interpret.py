import os

class Public:
    stubs = []
    _vars = {
        'A': None,
        'B': None,
        'C': None,
        'D': None,
        'E': None,
        'F': None,
        'G': None,
        'H': None,
        'I': None,
        'J': None,
        'K': None,
        'L': None,
        'M': None,
        'N': None,
        'O': None,
        'P': None,
        'Q': None,
        'R': None,
        'S': None,
        'T': None,
        'U': None,
        'V': None,
        'W': None,
        'X': None,
        'Y': None,
        'Z': None,
        }
    code = None
    line = None
    output = []

def parse_init(file_arg):
    Public.code = open(os.path.join(os.path.dirname(__file__), str(file_arg) + '.txt'), 'r')
    Public.line = list(Public.code.readline())

def parse():
    for i, char in enumerate(Public.line):
        if char == 'K':
            if 'D' in Public.stubs:
                Public.output.append(char)
                
            elif char in Public.stubs:
                del Public.stubs[Public.stubs.index('D')]
                Public.output.append(')')
                
            elif not char in Public.stubs:
                Public.stubs.append('K')
                Public.output.append('begin(')
                
        elif char == 'M':
            if 'D' in Public.stubs:
                Public.output.append(char)
                
            elif char in Public.stubs:
                del Public.stubs[Public.stubs.index('M')]
                Public.output.append(')')
                
            elif not char in Public.stubs:
                Public.stubs.append('M')
                Public.output.append('print(')
                
        elif char == 'D':
            
            if char in Public.stubs:
                del Public.stubs[Public.stubs.index('K')]
                Public.output.append(')')
                
            elif not char in Public.stubs:
                Public.stubs.append('D')
                Public.output.append('str(')
                
        else:
            if 'D' in Public.stubs:
                Public.output.append(char)
                print('Hello')
        print(Public.stubs)

    print(''.join(Public.output))
            
    
if __name__ == '__main__':
    parse_init('Alpha_Test.ala')
    parse()
