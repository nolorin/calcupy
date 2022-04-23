class Number:
	baseEncodeCharacters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'

	def __init__( self, value, base=10, encoded=False ):
		self.value = value
		self.base = base
		self.encoded = encoded

	def __str__( self ):
		places = []
		value = self.value
		while value > self.base:
			places.append( value % self.base )
			value //= self.base
		places.append( value );
		if self.base < 65:
			return ''.join( [ Number.baseEncodeCharacters[p] for p in places[::-1]] )
		else:
			return ':'.join( [ Number.baseEncodeCharacters[p//64] + Number.baseEncodeCharacters[p%64] for p in places[::-1]] )
			