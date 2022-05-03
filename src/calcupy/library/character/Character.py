import re

class Character:
	def __init__( self, value ):
		self.value = str( value )

	def __str__( self ):
		return self.value

	def __add__( self, other ):
		out = Character( self.value )
		out.value += other.value;
		return out;

	def __sub__( self, other ):
		out = Character( self.value )
		out.value = re.sub( r'{}'.format( other.value ), '', out.value );
		return out

	def __mul__( self, other ):
		pass

	def __truediv__( self, other ):
		pass

	def __floordiv__( self, other ):
		pass

	def __mod__( self, other ):
		pass

	def __divmod__( self, other ):
		pass

	def __pow__( self, other ):
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
