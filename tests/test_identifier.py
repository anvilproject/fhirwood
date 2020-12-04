import pytest

from fhirwood.identifier import Identifier

def test_identifier_param_init():
	id1 = Identifier(value='1234', system='our_system')
	id2 = Identifier(value='1234', system='our_system')
	id3 = Identifier(value='1234', system='their_system')
	id4 = Identifier(value='4321', system='our_system')

	assert(id1=='1234')
	assert(id1 != '3421')
	assert(id1 == id2)
	assert(id1 != id3)
	assert(id1 != id4)

	obj = id1.as_obj()
	assert(obj['value'] == '1234')
	assert(obj['system'] == 'our_system')

def test_identifier_block_init():
	id1 = Identifier(block={'value':'1234', 'system':'our_system'})
	id2 = Identifier(value='1234', system='our_system')
	id3 = Identifier(value='1234', system='their_system')
	id4 = Identifier(value='4321', system='our_system')

	assert(id1=='1234')
	assert(id1 != '3421')
	assert(id1 == id2)
	assert(id1 != id3)
	assert(id1 != id4)

	obj = id1.as_obj()
	assert(obj['value'] == '1234')
	assert(obj['system'] == 'our_system')

def test_identifier_block_array_init():
	id1 = Identifier(block=[{'value':'12345', 'system':'our_system'}, {'value': '2345', 'system': 'another_system'}])
	id2 = Identifier(value='12345', system='our_system')
	id3 = Identifier(value='12345', system='their_system')
	id4 = Identifier(value='4321', system='our_system')

	assert(id1=='12345')
	assert(id1 == '2345')
	assert(id1 != '3421')
	assert(id1 == id2)
	assert(id1 != id3)
	assert(id1 != id4)

	obj = id1.as_obj()
	assert(len(obj) == 2)
	assert(obj[0]['value'] == '12345')
	assert(obj[0]['system'] == 'our_system')

