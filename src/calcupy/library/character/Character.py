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
		out = Character( self.value & other.value )
		return out

	def __truediv__( self, other ):
		out = Character( self.value | other.value )
		return out

	def __floordiv__( self, other ):
		out = Character( self.value ^ other.value )
		return out

	def __mod__( self, other ):
		out = Character( self.value | ( self.value ^ other.value ) )
		return out

	def __divmod__( self, other ):
		return ( self // other, self % other )

	def __lshift__( self, other ):
		out = Character( self.value << other.value )
		return out

	def __rshift__( self, other ):
		out = Character( self.value >> other.value )
		return out

	def __and__( self, other ):
		return self * other

	def __xor__( self, other ):
		return self ^ other

	def __or__( self, other ):
		return self / other
