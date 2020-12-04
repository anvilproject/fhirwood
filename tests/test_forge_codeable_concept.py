import pytest

from fhirwood.codeable_concept import CodeableConcept 

def test_forge_codeable_concept_param_init():
	cc1 = CodeableConcept(text="asdf", coding={"code": "code1"})
	cc2 = CodeableConcept(text="asdf", coding={"code": "code1"})
	cc3 = CodeableConcept(text="fdsa", coding={"code": "code2"})
	cc4 = CodeableConcept(coding={'code': "code1"})


	assert(cc1 == "code1")
	assert(cc1 == cc2)
	assert(cc1 != cc3)
	assert(cc1 == cc4)