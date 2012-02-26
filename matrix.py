from vector import Vector as v

"""
A Matrix is an array of vectors
"""

class Matrix(object):
    
    def __init__(self, *rows):
        """
        Matrix(row1[, row2[, row3, ...]])
        Where row-i could be a list, tuple or vector with the same length
        """
        self.__rows = list()
        l = list() # l store the length of each row
        for row in rows:
            self.__rows.append(v(fila))
            l.append(len(v(fila)))
        
        if max(l) != min(l):
            raise ValueError, 'The rows have got differents sizes'

    def __add__(self, other):
        pass

    def __mul__(self, other):
        pass

    def transpose():
        return zip(*self.__rows)

    def tr

def homogenize():
