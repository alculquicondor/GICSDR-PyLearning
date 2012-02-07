"""
Date: Febrary 3, 2012
Authors:
	Frank Moreno - @kranfix
	Aldo Culquicondor - @alculquicondor
"""

class Vector():
    def __init__(self, *elems):
        'Receives multiple numerical arguments, lists or tuples'
        #Concatenating possible lists or tuples
        t=[]
        for x in elems:
            if isinstance(x, (tuple,list)):
                t[len(t):] = x
            else:
                t.append(x)
        elems=tuple(t)
        #Verifying that all the elements are numerical
        for x in elems:
            if not isinstance(x, (float,int)):
                raise ValueError, 'Elements must be numerical'
        self.__elems = elems
	
	def getElements(self, type="t"):
		"""
		type = "t" returns the vector like a tuple
		type = "l" returns the vector like a list
		"""
		if type == "t":
			return self.__vector
		elif type == "l":
			return list(self.__vector)

	def __str__(self):
		return str(self.__vector)

	def __unicode__(self):
		return unicode(self.__vector)

	def __len__(self):
		return len(self.__vector)
	
	def __add__(self, other):
		if not isinstance(other,Vector):
			raise TypeError, \
				'Operation not defined for '+type(other).__name__

		if len(self) != len(other):
			raise ValueError, \
				'Incompatible sizes for '+str(self)+' and '+str(other)
		a = self.get()
		b = other.get()
		return Vector(*[x+b[i] for i,x in enumerate(a)])

	def __mul__(self, other):
		if not isinstance(other,Vector):
			raise TypeError, \
				'Operation not defined for '+type(other).__name__
				
		if len(self) != len(other):
			raise ValueError, \
				'Incompatible sizes for '+str(self)+' and '+str(other)

		a = self.get()
		b = other.get()
		return Vector(*[x*b[i] for i,x in enumerate(a)])

	def __abs__(self):
		return (self.dot(self))**0.5
		
	def dot(self, other):
		"""return the dot product"""
		c = self * other
		return sum(c.getElements())


if __name__ == '__main__':
	a = Vector(1, 2, 3)
	b = Vector(4, 5, 6)
	c = a + b
	d = a * b
	e = dot(a, b)
	print a, "+", b, "=", c
	print a, "*", b, "=", d
	print a, ".*", b, "=", e
	print "abs(a) =", abs(a)
