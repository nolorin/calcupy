class Number:
	baseEncodeCharacters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'

	def __init__( self, value, base=10, encoded=False ):
		self.value = value
		self.base = base
		self.encoded = encoded

	def __str__( self ):
		out = ''
		if self.base < 64:
			chars = self.characterArray()
			for c in chars:
				out += Number.baseEncodeCharacters[c]
		return out

	def characterArray( self ):
		out = []
		value = self.value
		i = 0
		while value:
			step = self.value//pow( self.base, i+1 )
			out.append( step )
			print(value)
			value = step
			i += 1
		return out


yu = Number(1000,2)
print( yu.characterArray() )