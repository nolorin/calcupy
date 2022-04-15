def

class Number:
	encodeBase2 = '01'
	encodeBase8 = '01234567'
	encodeBase10 = '0123456789'
	encodeBase12 = '0123456789ab'
	encodeBase16 = '0123456789abcdef'
	encodeBase60 = '0123456789abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY'
	encodeBase60 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'

	def __init__( self, value=None, base=10, dataType='float' ):
		if type( value ) in [ int, float ]:
			self.value = bin( value )
		elif type( value ) == Number:
			self.value = value
		self.base = base
		self.dataType = dataType

	def convertBase( self, newBase:int ):
		if newBase > 0:
			this.base = newBase
			# Code

			return True
		else:
			return None

	def __add__( self, other ):
		pass

	def __sub__( self, other ):
		pass

	def __mul__( self, other ):
		pass

	def __matmul__( self, other ):
		pass

	def __truediv__( self, other ):
		pass

	def __floordiv__( self, other ):
		pass

	def __mod__( self, other ):
		pass

	def __divmod__( self, other ):
		pass

	def __pow__( self, other, modulo ):
		pass

	def __lshift__( self, other ):
		pass

	def __rshift__( self, other ):
		pass

	def __and__( self, other ):
		pass

	def __xor__( self, other ):
		pass

	def __or__( self, other ):
		pass


	def __neg__( self ):
		pass

	def __pos__( self ):
		pass

	def __abs__( self ):
		pass

	def __invert__( self ):
		pass


	def __complex__( self ):
		pass

	def __int__( self ):
		pass

	def __float__( self ):
		pass

