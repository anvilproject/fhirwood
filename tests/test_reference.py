import pytest

from fhirwood.reference import Reference

def test_reference_param_init():
	ref1 = Reference(ref="Patient/110")
	ref2 = Reference(ref="Patient/110")
	ref3 = Reference(ref="Patient/1321")

	assert(ref1 == "Patient/110")
	assert(ref1 == ref2)
	assert(ref1 != ref3)

	obj = ref1.as_obj()
	assert(obj['reference'] == "Patient/110")


def test_reference_block_init():
	ref1 = Reference(block={"reference": "Patient/110"})
	ref2 = Reference(block={"reference": "Patient/110"})
	ref3 = Reference(block={"reference": "Patient/1310"})

	assert(ref1 == "Patient/110")
	assert(ref1 == ref2)
	assert(ref1 != ref3)

	obj = ref1.as_obj()
	assert(obj['reference'] == "Patient/110")

# TODO test more complete examples