import pytest

from fhirwood.coding import Coding 

def test_forge_coding_param_init():
	c1 = Coding(code='A1', system='sys1', display='A1 Something')
	c2 = Coding(code='A1', system='sys1', display='A1 Some Other')
	c3 = Coding(code='A2', system='sys1', display='A2 something')
	c4 = Coding(code='A1', system='sys2', display='A1 something')

	assert(c1 == 'A1')
	assert(c1 != 'A2')
	assert(c1 == c2)
	assert(c1 != c3)
	assert(c1 != c4)

	obj = c1.as_obj()
	assert(obj['code'] == 'A1')
	assert(obj['system'] == 'sys1')

def test_forge_coding_param_init_as_array():
	c1 = Coding(code='A1', system='sys1', display='A1 Something', is_list=True)
	c2 = Coding(code='A1', system='sys1', display='A1 Some Other')
	c3 = Coding(code='A2', system='sys1', display='A2 something')
	c4 = Coding(code='A1', system='sys2', display='A1 something')

	assert(c1 == 'A1')
	assert(c1 != 'A2')
	assert(c1 == c2)
	assert(c1 != c3)
	assert(c1 != c4)

	obj = c1.as_obj()
	assert(obj[0]['code'] == 'A1')
	assert(obj[0]['system'] == 'sys1')
	assert(len(obj) == 1)

def test_forge_coding_block_init():
	c1 = Coding(block={'code':'A1', 'system':'sys1', 'display':'A1 Something'})
	c2 = Coding(code='A1', system='sys1', display='A1 Some Other')
	c3 = Coding(code='A2', system='sys1', display='A2 something')
	c4 = Coding(code='A1', system='sys2', display='A1 something')

	assert(c1 == 'A1')
	assert(c1 != 'A2')
	assert(c1 == c2)
	assert(c1 != c3)
	assert(c1 != c4)

	obj = c1.as_obj()
	assert(obj['code'] == 'A1')
	assert(obj['system'] == 'sys1')

def test_forge_coding_block_init_multi():
	c1 = Coding(block=[
			{'code':'A1', 'system':'sys1', 'display':'A1 Something'},
			{'code':'B10', 'system':'sysL', 'display':'Burritos'}
	])
	c2 = Coding(code='A1', system='sys1', display='A1 Some Other')
	c3 = Coding(code='A2', system='sys1', display='A2 something')
	c4 = Coding(code='A1', system='sys2', display='A1 something')

	assert(c1 == 'A1')
	assert(c1 == 'B10')
	assert(c1 != 'A2')
	assert(c1 == c2)
	assert(c1 != c3)
	assert(c1 != c4)

	obj = c1.as_obj()
	assert(len(obj) == 2)
	assert(obj[0]['code'] == 'A1')
	assert(obj[0]['system'] == 'sys1')
	assert(obj[1]['code'] == 'B10')
	assert(obj[1]['system'] == 'sysL')