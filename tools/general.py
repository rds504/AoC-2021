from os import path

def load_input(filename):

    data = ''

    with open(path.join('input', filename), 'r') as fd:
        data = fd.read()

    return data
