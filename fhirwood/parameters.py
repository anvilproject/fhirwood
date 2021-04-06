"""Python representation of a fhir Parameters object

A Parameters resource contains one or more parameter "objects"

Each parameter "object" consists of a name and and one or more of the following:
    valueX
    resource 
    part -- Part is basically an array of parameter objects

Rather than work through a truly generic mechanism for all possible
parameters, I'll add some specialized versions for the cases we encounter

ConceptMapParameter - Interprets the results from a conceptmap translate query
"""
import pdb
from fhirwood import FhirBase
from fhirwood.coding import Coding

class ConceptMapMatch(FhirBase):
    def __init__(self, block):
        assert block['name'] == "match"
        self.equivalence = None
        self.concept = None
        self.source = ""

        for part in block['part']:
            if part['name'] == "equivalence":
                self.equivalence = part['valueCode']
            elif part['name'] == "concept":
                self.concept = Coding(block=part['valueCoding'])
            elif part['name'] == "source":
                self.source = part['valueUri']


class ConceptMapParameter(FhirBase):
    def __init__(self, block):
        assert block['resourceType'] == "Parameters"
        self.result = False
        self.message = ''
        self.matches = []

        for chunk in block['parameter']:
            if chunk['name'] == 'result':
                self.result = chunk['valueBoolean']
            elif chunk['name'] == 'message':
                self.message = chunk['valueString']
            elif chunk['name'] == 'match':
                self.matches.append(ConceptMapMatch(chunk))

    @property
    def match_count(self):
        return len(self.matches)

    @property
    def match(self):
        if len(self.matches) > 0:
            return self.matches[0]
        return None
