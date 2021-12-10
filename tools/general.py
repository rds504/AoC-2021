from os import path

def load_input(filename):

    '''
    Load contents of a text file as a single string
    '''
    data = ''

    with open(path.join('input', filename), 'r') as fd:
        data = fd.read()

    return data

def load_ints(filename, base=10, delim=','):

    '''
    Load contents of a text file, interpreted as a list of integers
    '''
    return [int(i, base) for i in load_input(filename).split(delim)]

def load_strings(filename, delim='\n'):

    '''
    Load contents of a text filem interpreted as a list of strings
    '''
    return load_input(filename).split(delim)