"""Representation for CodeableConcept"""

from fhirwood import FhirBase
from fhirwood.coding import Coding

class CodeableConcept(FhirBase):
    def __init__(self, text=None, coding=None, block=None):
        self.text = text
        self.coding = None

        if coding:
            self.coding = Coding(block=coding) 

        if block:
            if "coding" in block:
                self.coding = Coding(block=block.get('coding'))
            
            self.text = block.get('text')

    def to_str(self):
        if self.text:
            return self.text
        return self.coding.display

    def __eq__(self, cc):
        if self.coding:
            if type(cc) is str:
                return self.coding == cc
            if cc.coding:
                return cc.coding == self.coding

        if type(cc) is str:
            return self.text == cc
        return self.text == cc.text



    def as_obj(self):
        obj = {}

        self.add_kv(obj, 'text')
        if self.coding:
            obj['coding'] = self.coding.as_obj()

        return obj
