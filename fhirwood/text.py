"""Simple text type"""
from fhirwood import FhirBase

class Text(FhirBase):
	def __init__(self, value=None, block=None):
		self.value = value

		if block is not None:
			self.value = block['text']

	def __eq__(self,  value):
		"Check to see if this matches the string or another text object"
		
		if type(value) is str:
			return self.value == value
			
		return self.value == value.value

	def as_obj(self):
		"Convert to generic object"

		return {
			"text": self.value
		}

			