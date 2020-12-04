"""Representation of the reference objects"""

from fhirwood import FhirBase

class Reference(FhirBase):
    def __init__(self, ref=None, reftype=None, identifier=None, display=None, block=None):
        self.ref = ref
        self.reftype = reftype
        self.identifier=identifier
        self.display = display
        self.alts = []

        if block is not None:
            if type(block) is list:
                self.extract_from_block(block[0])

                for other in block[1:]:
                    ref = Reference(block=other)
                    self.alts.append(ref)
            else:
                self.extract_from_block(block)

    def extract_from_block(self, block):
        self.ref = block.get('reference')
        self.value = block.get('value')
        self.system = block.get('system')
        self.idtype = block.get('type')

    def __eq__(self, ref):
        if type(ref) is str:
            # Comparing strings...first compare with ref and then identifier?
            does_match = ref == self.ref or ref==self.identifier

            if not does_match:
                for other in self.alts:
                    doees_match = does_match and (other==ref)

            return does_match

        if self.ref is not None:
            return self.ref == ref.ref

        return self.identifier == ref.identifier

    def as_obj(self):
        obj = {}

        self.add_kv(obj, 'reference', propname = 'ref')
        self.add_kv(obj, 'type', propname='reftype')
        self.add_kv(obj, 'identifier')
        self.add_kv(obj, 'display')

        return obj