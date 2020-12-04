import pytest

from fhirwood.range import Range 

def test_forge_range_param_init():
	r1 = Range(low=10)
	r2 = Range(low=10)
	r3 = Range(low=100)

	assert(r1 == 10)
	assert(r1 == r2)
	assert(r1 != r3)

	obj = r1.as_obj()
	assert(obj['low']['value'] == 10)

	r4 = Range(low=10, high=100)
	r5 = Range(low=10, high=100)
	r6 = Range(low=10, high=1000)
	r7 = Range(low=11, high=1000)

	assert(r4 == r5)
	assert(r4 != r1)
	assert(r4 != r6)
	assert(r4 != r7)

	obj = r4.as_obj()
	assert(obj['low']['value'] == 10)
	assert(obj['high']['value'] == 100)


def test_forge_range_block_init():
	r1 = Range(block = {"low":10})
	r2 = Range(low=10)
	r3 = Range(low=100)

	assert(r1 == 10)
	assert(r1 == r2)
	assert(r1 != r3)

	obj = r1.as_obj()
	assert(obj['low']['value'] == 10)

	r4 = Range(block = {"low":10, "high": 100})
	r5 = Range(low=10, high=100)
	r6 = Range(low=10, high=1000)
	r7 = Range(low=11, high=1000)

	assert(r4 == r5)
	assert(r4 != r1)
	assert(r4 != r6)
	assert(r4 != r7)

	obj = r4.as_obj()
	assert(obj['low']['value'] == 10)
	assert(obj['high']['value'] == 100)