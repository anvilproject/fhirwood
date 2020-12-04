import pytest

from fhirwood.text import Text 

def test_text_init_w_params():
	text1 = Text(value='ABC')
	text2 = Text(value='ABC')
	text3 = Text(value='CBA')

	assert(text1 == "ABC")
	assert(text1 != 'aB')
	assert(text1 == text2)
	assert(text1 != text3)

	obj = text1.as_obj()
	return obj['text'] == 'ABC'

def test_text_init_w_block():
	text1 = Text(block={"text": "123"})
	text2 = Text(value='123')
	text3 = Text(value='ABC')
	assert(text1 == "123")
	assert(text1 == text2)
	assert(text1 != text3)

	obj = text1.as_obj()
	return obj['text'] == '123'

