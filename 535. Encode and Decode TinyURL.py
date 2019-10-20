# 535. Encode and Decode TinyURL.py

# TinyURL is a URL shortening service where you enter a URL such as 
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. 
# There is no restriction on how your encode/decode algorithm should work. 
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

class Codec:

	def __init__(self):
		self.dict = {}
		self.dict_url = {}
		self.c = 0
		self.code = ""

	def encode(self, longUrl):
		"""Encodes a URL to a shortened URL.

		:type longUrl: str
		:rtype: str
		"""
		if longUrl not in self.dict_url:
			code = self.code + str(self.c)
			self.c = self.c + 1
			self.dict[code] = longUrl
			self.dict_url[longUrl] = code
		else:
			code = self.dict_url[longUrl]

		return code

	def decode(self, shortUrl):
		"""Decodes a shortened URL to its original URL.

		:type shortUrl: str
		:rtype: str
		"""
		return self.dict[shortUrl]
        
sol = Codec()
x = "https://leetcode.com/problems/design-tinyurl"
short_url = sol.encode(x)
print("origin: "+x)
print("encode: "+short_url)
original_url = sol.decode(short_url)
print("decode: "+original_url)

print("------")
url = "www.google.com"
short_url = sol.encode(url)
print("origin: "+url)
print("encode: "+short_url)
original_url = sol.decode(short_url)
print("decode: "+original_url)

print("------")
url = "www.google.com"
short_url = sol.encode(url)
print("origin: "+url)
print("encode: "+short_url)
original_url = sol.decode(short_url)
print("decode: "+original_url)

print("------")
url = "www.cosera.com"
short_url = sol.encode(url)
print("origin: "+url)
print("encode: "+short_url)
original_url = sol.decode(short_url)
print("decode: "+original_url)


print(sol.dict)
