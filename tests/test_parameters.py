import pytest

from fhirwood.coding import Coding 
from fhirwood.parameters import ConceptMapMatch, ConceptMapParameter

example_concept_map_param = {
  "resourceType": "Parameters",
  "parameter": [ {
    "name": "result",
    "valueBoolean": True
  }, {
    "name": "message",
    "valueString": "Matches found!"
  }, {
    "name": "match",
    "part": [ {
      "name": "equivalence",
      "valueCode": "equal"
    }, {
      "name": "concept",
      "valueCoding": {
        "system": "http://terminology.hl7.org/CodeSystem/v2-0001",
        "code": "M"
      }
    }, {
      "name": "source",
      "valueUri": "http://hl7.org/fhir/ConceptMap/cm-administrative-gender-v2"
    } ]
  } ]
}

failed_concept_match = {
  "resourceType": "Parameters",
  "parameter": [ {
    "name": "result",
    "valueBoolean": False
  }, {
    "name": "message",
    "valueString": "No matches found!"
  } ]
}

def test_concept_map_match():
    match = ConceptMapMatch(example_concept_map_param['parameter'][2])

    assert match.equivalence, "Should be a valid match"
    assert match.concept == "M"
    assert match.concept.system == "http://terminology.hl7.org/CodeSystem/v2-0001", "Verify that the target system is as is expected"
    assert match.source == "http://hl7.org/fhir/ConceptMap/cm-administrative-gender-v2"

def test_concept_map_parameter():
    match = ConceptMapParameter(example_concept_map_param)
    assert match.result, "Was a positive finding"
    assert match.message == "Matches found!"
    assert match.match_count == 1
    assert match.match.concept == "M", "Verify the first match found"

def test_concept_map_fail():
    match = ConceptMapParameter(failed_concept_match)
    assert not match.result, "Was a negative finding"
    assert match.message == "No matches found!"
    assert match.match_count == 0
    assert match.match is None, "Make sure None is returned if no matches were found"
