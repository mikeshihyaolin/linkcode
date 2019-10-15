# 1108. Defanging an IP Address.py

# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

 

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"


class Solution(object):
	# def defangIPaddr(self, address):
	# 	"""
	# 	:type address: str
	# 	:rtype: str
	# 	"""
	# 	res = ""

	# 	for s in address:
	# 		if s == ".":
	# 			res+="[.]"
	# 		else:
	# 			res+=s
	# 	return res

	def defangIPaddr(self, address):
		"""
		:type address: str
		:rtype: str
		"""

		return address.replace(".","[.]")

address = "1.1.1.1"
address = "255.100.50.0"

sol = Solution()
res = sol.defangIPaddr(address)
print(res)
