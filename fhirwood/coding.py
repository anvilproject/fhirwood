"""Python representation of a fhir Coding object

Coding objects should evaluate against either other code objects or strings. 

Coding objects must be able to contain multiple representations and test for equivalence against all of those. 

Coding objects should be able to cast themselves back to plain dictionaries in order to use in construction of JSON objects to submit to a FHIR server
"""
import pdb
from fhirwood import FhirBase

class Coding(FhirBase):
	def __init__(self, code=None, system=None, display=None, version=None, is_list=False, block=None):
		"""Forge a code object either directly using code/system params or from a block (dictionary)"""
		self.code = code
		self.system = system
		self.display = display
		self.version = version
		self.is_list = is_list

		# In case we have multiple codes that represent the same entity, we 
		# can capture the siblings here
		self.alts = []

		if block is not None:
			if type(block) is list:
				self.is_list = True
				self.extract_from_block(block[0])
				for entry in block[1:]:
					self.alts.append(Coding(block=entry))
			else:
				self.extract_from_block(block)

	def extract_from_block(self, block):
		self.code = block['code']
		if 'system' in block:
			self.system = block['system']
		if 'display' in block:
			self.display = block['display']		

	def __eq__(self,  code):
		"Check to see if the code matches this or any of it's alternates"

		#pdb.set_trace()
		is_same = False
		if type(code) is str:
			is_same = self.code == code
			if not is_same:
				is_same = self.display == code
		else:
			if self.system:
				is_same = (self.code == code.code) and (self.system==code.system)
			else:
				is_same = self.code == code.code

		if not is_same:
			for alt in self.alts:
				is_same = is_same or (alt == code)

		return is_same

	def as_obj(self):
		"Convert to generic object list suitable. If this is marked as a list, a list is returned"
		obj = {	}

		self.add_kv(obj, 'code')
		self.add_kv(obj, 'system')
		self.add_kv(obj, 'display')
		self.add_kv(obj, 'version')

		if self.is_list:
			objs = [obj]

			for alt in self.alts:
				objs.append(alt.as_obj())
			return objs
		return obj




