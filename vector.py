"""
Date: Febrary 22, 2012
Authors:
    Frank Moreno - @kranfix
    Aldo Culquicondor - @alculquicondor
"""

class Vector():
    """
    The Vector class represent a vector in Real n-dimension space
    in cartesian coordinate
    """
    def __init__(self, *elems):
        'Receives multiple numerical arguments, lists or tuples'
        #Concatenating possible lists or tuples
        self.__vector = list()  #empty list
        for x in elems:
            if isinstance(x, (tuple,list)):
                self.__vector[len(self.__vector):] = list(x)
            else:
                self.__vector.append(x)
        #Verifying that all the elements are numerical
        for x in self.__vector:
            if not isinstance(x, (float,int)):
                raise ValueError, 'Elements must be numerical'

    def __str__(self):
        return str(tuple(self.__vector))

    def __unicode__(self):
        return unicode(tuple(self.__vector))

    def __list__(self):
        'return the vector as a list'
        return self.__vector

    def __tuple__(self):
        'return a vector as a tuple'
        return tuple(vector.__vector)

    def __len__(self):
        'return the vector\'s length'
        return len(self.__vector)

    def __iter__(self):
        self.__index = -1
        return self

    def next(self):
        if self.__index == len(self)-1:
            raise StopIteration
        self.__index += 1
        return self.__vector[self.__index]

    def __add__(self, other):
        'The sum must be by two vector with the same length'
        if not isinstance(other,Vector):
            raise TypeError, \
                'Operation not defined for '+type(other).__name__

        if len(self) != len(other):
            raise ValueError, \
                'Incompatible sizes for '+str(self)+' and '+str(other)
        return Vector(*[x + y for x, y in zip(self, other)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[elem * other  for elem in self])
        if not isinstance(other,Vector):
            raise TypeError, \
                'Operation not defined for '+type(other).__name__
        if len(self) != len(other):
            raise ValueError, \
                'Incompatible sizes for '+str(self)+' and '+str(other)
        return Vector([x * y for x, y in zip(self, other)])

    def __abs__(self):
        return self.dot(self) ** 0.5

    def dot(self, other):
        'return the dot product'
        return sum(self*other)

if __name__ == '__main__':
    a = Vector(1, [2, 3])
    b = Vector((4, 5), 6)
    c = a + b
    d = a * b
    e = a.dot(b)
    print "Demos:"
    print a, "+", b, "=", c
    print a, "*", b, "=", d
    print a, ".*", b, "=", e
    print "abs(a) =", abs(a)
