class CharacterDiscrete( Character ):

	def __add__( self, other ):
		out = Character( self.value )
		out.value += other.value;
		return out;

	def __sub__( self, other ):
		out = Character( self.value )
		out.value += ~other.value
		return out

	def __mul__( self, other ):
		out = Character( self.value | other.value )
		return out

	def __truediv__( self, other ):
		out = Character( self.value ^ other.value )
		return out

	def __floordiv__( self, other ):
		return self / other

	def __mod__( self, other ):
		return Character( '' )

	def __lshift__( self, other ):
		return self

	def __rshift__( self, other ):
		return other

	def __and__( self, other ):
		return self + other

	def __xor__( self, other ):
		out = Character( ~self.value + ~other.value )
		return out

	def __or__( self, other ):
		return self - other
