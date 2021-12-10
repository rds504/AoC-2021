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
    data = []

    with open(path.join('input', filename), 'r') as fd:
        data = [int(i, base) for i in fd.read().split(delim)]

    return data