from functools import reduce
from operator import mul

def product(sequence):

    '''
    Find the product of elements in a sequence
    '''
    return reduce(mul, sequence)