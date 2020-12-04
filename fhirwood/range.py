"""Build range objects for/from fhir"""

from fhirwood import FhirBase 
from fhirwood.simple_quantity import SimpleQuantity

import pdb

class Range(FhirBase):
	def __init__(self, low=None, high=None, block=None):
		self.low = None
		self.high = None

		if low:
			self.low = SimpleQuantity(low)

		if high is not None:
			self.high = SimpleQuantity(high)

		if block is not None:
			print(block)
			if 'low' in block:
				self.low = SimpleQuantity(block=block['low'])
			if 'high' in block:
				self.high = SimpleQuantity(block=block['high'])

	def __eq__(self,  value):
		"Check to see if this matches the string or another text object"
		
		#pdb.set_trace()
		# This is a bit more complicated. Let's assume that a real range
		# can be separated by a "-"
		if type(value) is str:
			if "-" in value:
				low,high = value.split("-")

				return self.low == low and self.high == high
			return self.low == value

		if type(value) is Range:
			if self.high or value.high: 
				return self.high == value.high  and self.low==value.low
			return self.high is None and self.low == value.low

		# This can't work if the range has both high and low
		return (self.high is None) and (self.low == value)


	def as_obj(self):
		"Convert to generic object"

		repr = {
			"low" : self.low.as_obj()
		}
		if self.high:
			repr['high'] = self.high.as_obj()

		return repr
			