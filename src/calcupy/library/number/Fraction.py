class Fraction:
	def __init__( self, unit, base, lcd=True ):
		self.unit = unit
		self.base = base
		self.lcd_on = lcd

	def lcd( self ):
		if self.lcd_on:
			i = self.base
			while i > 0:
				if [ self.unit % i, self.base % i ] == [ 0, 0 ]:
					self.unit //= i
					self.base //= i

	def __add__( self, other ):
		out = Fraction( 0, 0, self.lcd_on )
		if self.base != other.base:
			[ out.unit, out.base ] = [ ( self.unit*other.base ) + other.unit, self.base*other.base ]
			out.lcd()
		else:
			out.unit += other.unit
		return out

	def __sub__( self, other ):
		out = Fraction( 0, 0, self.lcd_on )
		if self.base != other.base:
			[ self.unit, self.base ] = [ ( self.unit*other.base ) - other.unit, self.base*other.base ]
			self.lcd()
		else:
			self.unit += other.unit
		return out

	def __mul__( self, other ):
		out = Fraction( self.unit*other.unit, self.base*other.base, self.lcd_on )
		out.lcd()
		return out

	def __truediv__( self, other ):
		out = Fraction( self.unit*other.base, self.base*other.unit, self.lcd_on )
		out.lcd()
		return out

	def __floordiv__( self, other ):
		meta = Fraction( self.unit*other.base, self.base*other.unit, self.lcd_on )
		meta.lcd()
		out = Fraction( meta.unit // meta.base, meta.base, False )
		return out

	def __mod__( self, other ):
		out = Fraction( 0, 0, self.lcd_on )
		return ( self / other ) - ( self // other )

	def __divmod__( self, other ):
		return ( self // other, self % other )

	def __pow__( self, other ):
		return ( self.unit / self.base ) ** ( other.unit / other.base )

	def __lshift__( self, other ):
		return Fraction( self.unit << other.unit, self.base << other.base, self.lcd_on )

	def __rshift__( self, other ):
		return Fraction( self.unit >> other.unit, self.base >> other.base, self.lcd_on )

	def __and__( self, other ):
		snum = self.unit / self.base
		onum = self.unit / self.base
		return snum and onum

	def __xor__( self, other ):
		snum = self.unit / self.base
		onum = self.unit / self.base
		return snum ^ onum

	def __or__( self, other ):
		snum = self.unit / self.base
		onum = self.unit / self.base
		return snum or onum

class F( Fraction ):
	pass