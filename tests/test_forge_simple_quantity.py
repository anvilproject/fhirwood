import pytest

from fhirwood.simple_quantity import SimpleQuantity 

def test_sq_init_params_basic():
	sq1 = SimpleQuantity(value=15)
	sq2 = SimpleQuantity(value=15)
	sq3 = SimpleQuantity(value=1500)

	assert(sq1 == 15)
	assert(sq1 == "15")
	assert(sq1 == sq2)
	assert(sq1 != sq3)

	obj = sq1.as_obj()
	assert(obj['value'] == 15)

def test_sq_init_block_basic():
	sq1 = SimpleQuantity(block={"value": 15})
	sq2 = SimpleQuantity(block={"value": 15})
	sq3 = SimpleQuantity(block={"value": 150})

	assert(sq1 == "15")
	assert(sq1 == 15)
	assert(sq1 == sq2)
	assert(sq1 != sq3)

	obj = sq1.as_obj()
	assert(obj['value'] == 15)

# TODO work out tests for more complete examples of these objects