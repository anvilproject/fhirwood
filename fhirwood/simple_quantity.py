"""Represent the fhir SimpleQuantity object"""

from fhirwood import FhirBase
from fhirwood.coding import Coding

class SimpleQuantity(FhirBase):
    def __init__(self, value=None, unit=None, system=None, code=None, block=None):
        self.value = value
        self.unit = unit
        self.system = system
        self.code = code

        if block is not None:
            self.value = block.get('value')
            self.unit = block.get('unit')
            self.system = block.get('system')

            if 'code' in block:
                self.code = Coding(block.get('code'))

    def __eq__(self,  value):
        "Check to see if this matches the string or another text object"
        
        if value is None:
            return False
        # This is a bit more complicated. Let's assume that a real range
        # can be separated by a "-"
        if type(value) is str:
            return self.value == float(value)

        if type(value) in [int, float]:
            return self.value == value

        return self.value == value.value

    def as_obj(self):
        "Convert to generic object"

        repr = {
            "value": self.value
        }

        self.add_kv(repr, 'unit')
        self.add_kv(repr, 'system')

        if self.code:
            repr['code'] = self.code.as_obj()

        return repr

            