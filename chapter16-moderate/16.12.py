# Test
# 16.12 XML Encoding Since XML is very verbose, you are given a way of encoding it where
# each tag gets mapped to a pre-defined integer value. The language/grammar is as follows:
# Element --> Tag Attributes END Children END
# Attribute --> Tag Value
# END --> 0
# Tag --> some predefined mapping to int
# Value --> string value END
# For example, the following XML might be converted into the compressed string below
# (assuming a mapping of family -> 1, person -> 2, firstName -> 3, lastName -> 4, state -> 5).
# <family lastName="McDowell" state="CA">
# 	<person firstName="Gayle">Some Message</person>
# </family>
# Becomes:
# 1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0.
# Write code to print the encoded version of an XML element (passed in Element and Attribute objects).

class Element:
	"""
	>>> e1 = Element("family", Attribute("lastName", "McDowell"), Attribute("state", "CA"))
	>>> e2 = Element("person", Attribute("firstName", "Gayle"))
	>>> e1.set_child(e2)
	>>> e2.set_child("Some Message")
	>>> " ".join(e1.encoded_version())
	'1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0'
	"""
	string_map = {
		"family": "1",
		"person": "2",
		"firstName": "3",
		"lastName": "4",
		"state": "5"
	}

	def __init__(self, tag, *attributes):
		self.tag = tag
		self.attributes = attributes
		self.children = []

	def set_child(self, child):
		self.children.append(child)

	def encoded_version(self):
		encoded_arr = []
		# Element --> Tag Attributes END Children END
		encoded_arr.append(self.string_map[self.tag])
		for i in range(len(self.attributes)):
			encoded_arr.extend(self.attributes[i].encoded_version())
		encoded_arr.append("0")
		for i in range(len(self.children)):
			if isinstance(self.children[i], str):
				encoded_arr.append(self.children[i])
			else:
				encoded_arr.extend(self.children[i].encoded_version())
		encoded_arr.append("0")
		return encoded_arr


class Attribute:
	string_map = {
		"family": "1",
		"person": "2",
		"firstName": "3",
		"lastName": "4",
		"state": "5"
	}

	def __init__(self, tag, value):
		self.tag = tag
		self.value = value

	def encoded_version(self):
		# Attribute --> Tag Value
		return [self.string_map[self.tag], self.value]

if __name__ == "__main__":
	import doctest
	doctest.testmod()
