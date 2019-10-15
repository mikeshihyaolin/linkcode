# 535. Encode and Decode TinyURL.py

# TinyURL is a URL shortening service where you enter a URL such as 
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. 
# There is no restriction on how your encode/decode algorithm should work. 
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

class Codec:

	def __init__(self):
		self.dict = {}
		self.c = 0
		self.code = "www.tinyurl."

	def encode(self, longUrl):
		"""Encodes a URL to a shortened URL.

		:type longUrl: str
		:rtype: str
		"""
		if longUrl not in self.dict:
			code = self.code + str(self.c)
			self.c = self.c + 1
			self.dict[code] = longUrl

		return code


	def decode(self, shortUrl):
		"""Decodes a shortened URL to its original URL.

		:type shortUrl: str
		:rtype: str
		"""
		return self.dict[shortUrl]
        
sol = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
short_url = sol.encode(url)
print(short_url)
original_url = sol.decode(short_url)
print(original_url)

