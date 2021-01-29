"""Basic identifier representation"""

from fhirwood import FhirBase 

import pdb

class Identifier(FhirBase):
    def __init__(self, 
                    value=None, 
                    system=None, 
                    idtype=None, 
                    is_list=False,
                    block=None):
        self.value = value
        self.system = system
        self.idtype = idtype
        self.is_list = is_list

        self.alts = []

        if block:
            if type(block) is list:
                self.is_list = True

                self.extract_from_block(block[0])

                for entry in block[1:]:
                    self.alts.append(Identifier(block=entry))
            else:
                self.extract_from_block(block)

    def extract_from_block(self, block):
        self.value = block.get('value')
        self.system = block.get('system')
        self.idtype = block.get('type')

    def get_identifiers(self):
        return [self.value] + self.alts

    def __eq__(self, other):
        does_match = False

        if type(other) is str:
            does_match = self.value == other
        elif self.system or other.system:
            does_match = (self.value==other.value) and (self.system==other.system)
        else:
            does_match = self.value == other.value

        if not does_match:
            for alt in self.alts:
                does_match = does_match or alt == other

        return does_match

    def as_obj(self):
        obj = {}

        self.add_kv(obj, 'value')
        self.add_kv(obj, 'system')
        self.add_kv(obj, key='type', propname='idtype')

        if self.is_list:
            objs = [obj]

            for alt in self.alts:
                objs.append(alt.as_obj)

            return objs
        return obj
