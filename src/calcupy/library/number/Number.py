class Number:
	baseEncodeCharacters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'

	def __init__( self, value, base=10, encoded=False ):
		self.value = value
		self.base = base
		self.encoded = encoded

	def __str__( self ):
		out = ''

		return out
